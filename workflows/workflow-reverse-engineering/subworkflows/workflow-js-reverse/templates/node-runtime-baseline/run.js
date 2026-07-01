async function main() {
  function add(a, b) {
    return a + b;
  }

  const result = {
    runtime: "node",
    syncResult: add(18, 24),
    promiseResult: await Promise.resolve("node-promise-ok")
  };

  console.log(JSON.stringify(result));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
