#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

function parseArgs(argv) {
  const result = { scopes: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--vault") {
      result.vault = argv[++i];
    } else if (arg === "--scope") {
      result.scopes.push(argv[++i]);
    } else if (arg === "--json") {
      result.json = true;
    } else if (arg === "--help" || arg === "-h") {
      result.help = true;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }
  return result;
}

function walkFiles(root) {
  const output = [];
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    if (entry.name === ".git" || entry.name === "node_modules") continue;
    const fullPath = path.join(root, entry.name);
    if (entry.isDirectory()) {
      output.push(...walkFiles(fullPath));
    } else {
      output.push(fullPath);
    }
  }
  return output;
}

function normalizePath(input) {
  return path.resolve(input);
}

function resolveExplicitTarget(vault, target) {
  const candidate = path.join(vault, target);
  if (path.extname(candidate)) return fs.existsSync(candidate) ? [candidate] : [];
  const markdownCandidate = `${candidate}.md`;
  return fs.existsSync(markdownCandidate) ? [markdownCandidate] : [];
}

function extractHeadings(filePath) {
  if (!filePath.endsWith(".md")) return [];
  return fs
    .readFileSync(filePath, "utf8")
    .split(/\r?\n/)
    .filter((line) => /^#{1,6}\s+/.test(line))
    .map((line) => line.replace(/^#{1,6}\s+/, "").trim());
}

function validate({ vault, scopes }) {
  const allFiles = walkFiles(vault);
  const basenameIndex = new Map();

  for (const filePath of allFiles) {
    const key = path.basename(filePath, path.extname(filePath));
    if (!basenameIndex.has(key)) basenameIndex.set(key, []);
    basenameIndex.get(key).push(filePath);
  }

  const sourceFiles = (scopes.length ? scopes : [vault])
    .flatMap((scope) => {
      const resolved = normalizePath(scope);
      if (!fs.existsSync(resolved)) {
        throw new Error(`Scope does not exist: ${resolved}`);
      }
      return fs.statSync(resolved).isDirectory() ? walkFiles(resolved) : [resolved];
    })
    .filter((filePath) => filePath.endsWith(".md"));

  const missing = [];
  const badHeadings = [];
  const ambiguous = [];
  let linksChecked = 0;

  for (const source of [...new Set(sourceFiles)]) {
    const text = fs.readFileSync(source, "utf8");
    const wikiLinkPattern = /!?\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g;
    for (const match of text.matchAll(wikiLinkPattern)) {
      linksChecked += 1;
      const rawTarget = match[1].trim();
      const hashIndex = rawTarget.indexOf("#");
      const target =
        hashIndex >= 0 ? rawTarget.slice(0, hashIndex).trim() : rawTarget;
      const heading =
        hashIndex >= 0 ? rawTarget.slice(hashIndex + 1).trim() : "";

      if (!target) continue;

      const matches = target.includes("/")
        ? resolveExplicitTarget(vault, target)
        : basenameIndex.get(path.basename(target, path.extname(target))) || [];

      if (matches.length === 0) {
        missing.push({ source, target: rawTarget });
        continue;
      }

      if (matches.length > 1 && !target.includes("/")) {
        ambiguous.push({ source, target: rawTarget, matches });
        continue;
      }

      if (heading && !extractHeadings(matches[0]).includes(heading)) {
        badHeadings.push({ source, target: rawTarget, file: matches[0] });
      }
    }
  }

  return {
    sourceFiles: new Set(sourceFiles).size,
    linksChecked,
    missing,
    badHeadings,
    ambiguous,
  };
}

function printHelp() {
  console.log(`Usage:
  node validate_obsidian_links.js --vault PATH [--scope PATH ...] [--json]

Options:
  --vault PATH  Obsidian vault or common link root
  --scope PATH  File or directory to validate; repeatable
  --json        Print JSON only`);
}

function main() {
  try {
    const args = parseArgs(process.argv.slice(2));
    if (args.help) {
      printHelp();
      return;
    }
    if (!args.vault) throw new Error("--vault is required");

    const vault = normalizePath(args.vault);
    if (!fs.existsSync(vault) || !fs.statSync(vault).isDirectory()) {
      throw new Error(`Vault is not a directory: ${vault}`);
    }

    const result = validate({
      vault,
      scopes: args.scopes.map(normalizePath),
    });
    const failed =
      result.missing.length +
        result.badHeadings.length +
        result.ambiguous.length >
      0;

    if (args.json) {
      console.log(JSON.stringify(result, null, 2));
    } else {
      console.log(`Source files: ${result.sourceFiles}`);
      console.log(`WikiLinks checked: ${result.linksChecked}`);
      console.log(`Missing targets: ${result.missing.length}`);
      console.log(`Bad headings: ${result.badHeadings.length}`);
      console.log(`Ambiguous targets: ${result.ambiguous.length}`);
      for (const [label, items] of [
        ["MISSING", result.missing],
        ["BAD_HEADING", result.badHeadings],
        ["AMBIGUOUS", result.ambiguous],
      ]) {
        for (const item of items) {
          console.log(`${label}: ${item.source} -> ${item.target}`);
        }
      }
    }
    process.exitCode = failed ? 1 : 0;
  } catch (error) {
    console.error(error.message);
    process.exitCode = 2;
  }
}

main();
