/*
 * Frida Java Crypto probe.
 *
 * Copy this file into a TASK directory before editing or running it.
 * It observes common Java crypto APIs and emits JSON lines that can be
 * used as candidate fixtures for reproduce-android-crypto.
 *
 * Default behavior is observe-only and redacted:
 * - original implementations are called and returned;
 * - raw input/key/iv bytes are not printed by default;
 * - previews, lengths and hashes are emitted for triage.
 */

var CRYPTO_PROBE_CONFIG = {
  schema: "android.crypto_probe.v1",
  windowId: "manual-window-001",
  processName: null,
  previewBytes: 32,
  raw: false,
  stack: false,
  modules: {
    messageDigest: true,
    mac: true,
    cipher: true,
    keyIv: true,
    base64: false
  }
};

Java.perform(function () {
  var eventSeq = 0;

  function nowMs() {
    return Date.now();
  }

  function nextEventId() {
    eventSeq += 1;
    return "crypto-probe-" + ("000000" + eventSeq).slice(-6);
  }

  function currentThreadId() {
    try {
      return Java.use("java.lang.Thread").currentThread().getId();
    } catch (e) {
      return null;
    }
  }

  function currentProcessName() {
    if (CRYPTO_PROBE_CONFIG.processName) return CRYPTO_PROBE_CONFIG.processName;
    try {
      return Java.androidContext.getPackageName().toString();
    } catch (e) {
      return null;
    }
  }

  function byteToHex(b) {
    var v = b;
    if (v < 0) v += 256;
    return ("0" + v.toString(16)).slice(-2);
  }

  function bytesToHex(bytes, limit) {
    if (bytes === null || bytes === undefined) return null;
    var n = Math.min(bytes.length, limit === undefined ? bytes.length : limit);
    var out = [];
    for (var i = 0; i < n; i++) out.push(byteToHex(bytes[i]));
    return out.join("");
  }

  function bytesToBase64(bytes) {
    if (bytes === null || bytes === undefined) return null;
    try {
      var Base64 = Java.use("android.util.Base64");
      return Base64.encodeToString(bytes, 2).toString();
    } catch (e) {
      return null;
    }
  }

  function bytesToUtf8Preview(bytes, limit) {
    if (bytes === null || bytes === undefined) return null;
    try {
      var n = Math.min(bytes.length, limit);
      var copy = Java.array("byte", Array.prototype.slice.call(bytes, 0, n));
      var StringCls = Java.use("java.lang.String");
      var s = StringCls.$new(copy, "UTF-8").toString();
      return s.length > 160 ? s.slice(0, 160) + "..." : s;
    } catch (e) {
      return null;
    }
  }

  function sha256Hex(bytes) {
    if (bytes === null || bytes === undefined) return null;
    try {
      var MessageDigest = Java.use("java.security.MessageDigest");
      var digest = MessageDigest.getInstance("SHA-256");
      var out = digest.digest(bytes);
      return bytesToHex(out);
    } catch (e) {
      return null;
    }
  }

  function summarizeBytes(bytes, includeRaw) {
    if (bytes === null || bytes === undefined) {
      return { length: 0, hex_preview: null, utf8_preview: null, sha256: null };
    }
    var summary = {
      length: bytes.length,
      hex_preview: bytesToHex(bytes, CRYPTO_PROBE_CONFIG.previewBytes),
      utf8_preview: bytesToUtf8Preview(bytes, CRYPTO_PROBE_CONFIG.previewBytes),
      sha256: sha256Hex(bytes)
    };
    if (includeRaw || CRYPTO_PROBE_CONFIG.raw) {
      summary.hex = bytesToHex(bytes);
      summary.base64 = bytesToBase64(bytes);
    }
    return summary;
  }

  function stackInfo() {
    if (!CRYPTO_PROBE_CONFIG.stack) {
      return { enabled: false, hash: null, top: [] };
    }
    try {
      var Throwable = Java.use("java.lang.Throwable");
      var Log = Java.use("android.util.Log");
      var s = Log.getStackTraceString(Throwable.$new()).toString();
      var lines = s.split("\n").slice(0, 16);
      var StringCls = Java.use("java.lang.String");
      var bytes = StringCls.$new(s).getBytes("UTF-8");
      return { enabled: true, hash: sha256Hex(bytes), top: lines };
    } catch (e) {
      return { enabled: true, hash: null, top: [], error: String(e) };
    }
  }

  function emit(category, className, methodName, operation, extra) {
    var event = {
      schema: CRYPTO_PROBE_CONFIG.schema,
      event_id: nextEventId(),
      timestamp_ms: nowMs(),
      process: currentProcessName(),
      thread_id: currentThreadId(),
      window_id: CRYPTO_PROBE_CONFIG.windowId,
      category: category,
      class: className,
      method: methodName,
      operation: operation,
      stack: stackInfo(),
      sensitivity: {
        raw_saved: !!CRYPTO_PROBE_CONFIG.raw,
        redacted: !CRYPTO_PROBE_CONFIG.raw
      }
    };
    for (var k in extra) event[k] = extra[k];
    console.log(JSON.stringify(event));
  }

  function safeHook(label, fn) {
    try {
      fn();
      console.log(JSON.stringify({ schema: CRYPTO_PROBE_CONFIG.schema, type: "probe_hooked", target: label }));
    } catch (e) {
      console.log(JSON.stringify({ schema: CRYPTO_PROBE_CONFIG.schema, type: "probe_skip", target: label, error: String(e) }));
    }
  }

  if (CRYPTO_PROBE_CONFIG.modules.messageDigest) {
    safeHook("java.security.MessageDigest", function () {
      var MessageDigest = Java.use("java.security.MessageDigest");

      MessageDigest.getInstance.overload("java.lang.String").implementation = function (algorithm) {
        var result = this.getInstance(algorithm);
        emit("message_digest", "java.security.MessageDigest", "getInstance", "init", {
          algorithm: algorithm ? algorithm.toString() : null
        });
        return result;
      };

      MessageDigest.update.overload("[B").implementation = function (input) {
        emit("message_digest", "java.security.MessageDigest", "update", "update", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          input: summarizeBytes(input, false)
        });
        return this.update(input);
      };

      MessageDigest.digest.overload().implementation = function () {
        var output = this.digest();
        emit("message_digest", "java.security.MessageDigest", "digest", "final", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          output: summarizeBytes(output, true)
        });
        return output;
      };

      MessageDigest.digest.overload("[B").implementation = function (input) {
        var output = this.digest(input);
        emit("message_digest", "java.security.MessageDigest", "digest", "final", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          input: summarizeBytes(input, false),
          output: summarizeBytes(output, true)
        });
        return output;
      };
    });
  }

  if (CRYPTO_PROBE_CONFIG.modules.keyIv) {
    safeHook("javax.crypto.spec.SecretKeySpec", function () {
      var SecretKeySpec = Java.use("javax.crypto.spec.SecretKeySpec");
      SecretKeySpec.$init.overload("[B", "java.lang.String").implementation = function (key, algorithm) {
        emit("key", "javax.crypto.spec.SecretKeySpec", "$init", "construct", {
          algorithm: algorithm ? algorithm.toString() : null,
          key: summarizeBytes(key, false)
        });
        return this.$init(key, algorithm);
      };
    });

    safeHook("javax.crypto.spec.IvParameterSpec", function () {
      var IvParameterSpec = Java.use("javax.crypto.spec.IvParameterSpec");
      IvParameterSpec.$init.overload("[B").implementation = function (iv) {
        emit("iv", "javax.crypto.spec.IvParameterSpec", "$init", "construct", {
          iv: summarizeBytes(iv, false)
        });
        return this.$init(iv);
      };
    });
  }

  if (CRYPTO_PROBE_CONFIG.modules.cipher) {
    safeHook("javax.crypto.Cipher", function () {
      var Cipher = Java.use("javax.crypto.Cipher");

      Cipher.getInstance.overload("java.lang.String").implementation = function (transformation) {
        var result = this.getInstance(transformation);
        emit("cipher", "javax.crypto.Cipher", "getInstance", "init", {
          algorithm: transformation ? transformation.toString() : null
        });
        return result;
      };

      Cipher.update.overload("[B").implementation = function (input) {
        var output = this.update(input);
        emit("cipher", "javax.crypto.Cipher", "update", "update", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          input: summarizeBytes(input, false),
          output: summarizeBytes(output, true)
        });
        return output;
      };

      Cipher.doFinal.overload().implementation = function () {
        var output = this.doFinal();
        emit("cipher", "javax.crypto.Cipher", "doFinal", "final", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          output: summarizeBytes(output, true)
        });
        return output;
      };

      Cipher.doFinal.overload("[B").implementation = function (input) {
        var output = this.doFinal(input);
        emit("cipher", "javax.crypto.Cipher", "doFinal", "final", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          input: summarizeBytes(input, false),
          output: summarizeBytes(output, true)
        });
        return output;
      };
    });
  }

  if (CRYPTO_PROBE_CONFIG.modules.mac) {
    safeHook("javax.crypto.Mac", function () {
      var Mac = Java.use("javax.crypto.Mac");

      Mac.getInstance.overload("java.lang.String").implementation = function (algorithm) {
        var result = this.getInstance(algorithm);
        emit("mac", "javax.crypto.Mac", "getInstance", "init", {
          algorithm: algorithm ? algorithm.toString() : null
        });
        return result;
      };

      Mac.update.overload("[B").implementation = function (input) {
        emit("mac", "javax.crypto.Mac", "update", "update", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          input: summarizeBytes(input, false)
        });
        return this.update(input);
      };

      Mac.doFinal.overload().implementation = function () {
        var output = this.doFinal();
        emit("mac", "javax.crypto.Mac", "doFinal", "final", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          output: summarizeBytes(output, true)
        });
        return output;
      };

      Mac.doFinal.overload("[B").implementation = function (input) {
        var output = this.doFinal(input);
        emit("mac", "javax.crypto.Mac", "doFinal", "final", {
          algorithm: this.getAlgorithm ? this.getAlgorithm().toString() : null,
          input: summarizeBytes(input, false),
          output: summarizeBytes(output, true)
        });
        return output;
      };
    });
  }

  if (CRYPTO_PROBE_CONFIG.modules.base64) {
    safeHook("android.util.Base64", function () {
      var Base64 = Java.use("android.util.Base64");
      Base64.decode.overload("java.lang.String", "int").implementation = function (input, flags) {
        var output = this.decode(input, flags);
        emit("base64", "android.util.Base64", "decode", "decode", {
          flags: flags,
          input_preview: input ? input.toString().slice(0, 160) : null,
          output: summarizeBytes(output, false)
        });
        return output;
      };
    });
  }
});
