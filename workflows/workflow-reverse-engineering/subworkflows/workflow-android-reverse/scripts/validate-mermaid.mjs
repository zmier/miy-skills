import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { basename, join, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const projectRoot = resolve(import.meta.dirname, "..");
const defaultFiles = [
  "skills/android-request-reproduction/assets/request-construction-ledger-template.md",
];
const files = process.argv.length > 2 ? process.argv.slice(2) : defaultFiles;
const mmdc = join(projectRoot, "node_modules", ".bin", "mmdc");
const tempRoot = mkdtempSync(join(tmpdir(), "android-reverse-mermaid-"));
let blockCount = 0;

try {
  for (const input of files) {
    const markdownPath = resolve(projectRoot, input);
    const markdown = readFileSync(markdownPath, "utf8");
    const blocks = [...markdown.matchAll(/```mermaid\s*\n([\s\S]*?)```/g)];

    if (blocks.length === 0) {
      throw new Error(`${markdownPath}: 未找到 Mermaid 代码块`);
    }

    for (const [index, match] of blocks.entries()) {
      blockCount += 1;
      const stem = `${basename(markdownPath, ".md")}-${index + 1}`;
      const inputPath = join(tempRoot, `${stem}.mmd`);
      const outputPath = join(tempRoot, `${stem}.svg`);
      writeFileSync(inputPath, `${match[1].trimEnd()}\n`, "utf8");

      const result = spawnSync(
        mmdc,
        ["--input", inputPath, "--output", outputPath, "--quiet"],
        { cwd: projectRoot, encoding: "utf8" },
      );

      if (result.status !== 0) {
        const detail = [result.stdout, result.stderr].filter(Boolean).join("\n");
        throw new Error(
          `${markdownPath} 的 Mermaid 代码块 ${index + 1} 渲染失败\n${detail}`,
        );
      }

      console.log(`PASS ${markdownPath}#mermaid-${index + 1}`);
    }
  }

  console.log(`Mermaid validation passed: ${blockCount} block(s).`);
} finally {
  rmSync(tempRoot, { recursive: true, force: true });
}
