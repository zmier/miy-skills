Java.perform(function () {
  var Throwable = Java.use("java.lang.Throwable");
  var Log = Java.use("android.util.Log");
  var classes = [
    "java.util.HashMap",
    "java.util.LinkedHashMap",
    "java.util.TreeMap"
  ];
  var keyPattern = /(data|sign|token|session|body|params|payload|sk|sh-|header)/i;

  function summarize(value) {
    if (value === null || value === undefined) return "null";
    var s = value.toString();
    if (s.length > 240) s = s.slice(0, 240) + "...";
    return s;
  }

  function stack() {
    return Log.getStackTraceString(Throwable.$new()).toString();
  }

  classes.forEach(function (name) {
    try {
      var MapClass = Java.use(name);
      MapClass.put.implementation = function (key, value) {
        var keyText = summarize(key);
        if (keyPattern.test(keyText)) {
          console.log(JSON.stringify({
            kind: "map_put",
            mapClass: name,
            key: keyText,
            valuePreview: summarize(value),
            stack: stack()
          }));
        }
        return this.put(key, value);
      };
    } catch (e) {
      console.log(JSON.stringify({ kind: "map_put_probe_skip", className: name, error: String(e) }));
    }
  });
});
