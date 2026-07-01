Java.perform(function () {
  var Base64 = Java.use("android.util.Base64");

  function previewBytes(bytes) {
    if (bytes === null || bytes === undefined) return "null";
    var n = Math.min(bytes.length, 32);
    var out = [];
    for (var i = 0; i < n; i++) {
      var b = bytes[i];
      if (b < 0) b += 256;
      out.push(("0" + b.toString(16)).slice(-2));
    }
    return out.join("") + (bytes.length > n ? "..." : "");
  }

  Base64.encodeToString.overload("[B", "int").implementation = function (input, flags) {
    var result = this.encodeToString(input, flags);
    console.log(JSON.stringify({
      kind: "base64_encodeToString",
      inputLength: input ? input.length : 0,
      inputHexPreview: previewBytes(input),
      flags: flags,
      outputPreview: result ? result.toString().slice(0, 160) : "null"
    }));
    return result;
  };

  Base64.decode.overload("java.lang.String", "int").implementation = function (input, flags) {
    var result = this.decode(input, flags);
    console.log(JSON.stringify({
      kind: "base64_decode",
      inputPreview: input ? input.toString().slice(0, 160) : "null",
      flags: flags,
      outputLength: result ? result.length : 0,
      outputHexPreview: previewBytes(result)
    }));
    return result;
  };
});
