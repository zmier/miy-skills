// Frida channel probe template.
// Fill target classes/methods from static evidence before running.

Java.perform(function () {
  function logStack(tag) {
    var Log = Java.use("android.util.Log");
    var Exception = Java.use("java.lang.Exception");
    console.log(tag + "\n" + Log.getStackTraceString(Exception.$new()));
  }

  console.log("[channel-probe] loaded");

  // Example:
  // var Cls = Java.use("com.example.TargetBridge");
  // Cls.call.overload("java.lang.String", "java.lang.String").implementation = function (name, payload) {
  //   console.log("[bridge] name=" + name + " payload=" + payload);
  //   logStack("[bridge stack]");
  //   return this.call(name, payload);
  // };
});
