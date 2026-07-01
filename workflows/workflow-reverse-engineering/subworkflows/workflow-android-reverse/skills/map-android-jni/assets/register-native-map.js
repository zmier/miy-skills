'use strict';

var REGISTER_NATIVE_MAP_CONFIG = {
  schema: 'android.jni_register_map.v1',
  targetClass: '__TARGET_CLASS__',
  includeAllClasses: false,
  includeCandidates: true
};

function shouldKeepClass(className) {
  if (REGISTER_NATIVE_MAP_CONFIG.includeAllClasses) return true;
  if (!REGISTER_NATIVE_MAP_CONFIG.targetClass || REGISTER_NATIVE_MAP_CONFIG.targetClass === '__TARGET_CLASS__') return true;
  return className === REGISTER_NATIVE_MAP_CONFIG.targetClass;
}

function emit(type, payload) {
  var event = {
    schema: REGISTER_NATIVE_MAP_CONFIG.schema,
    type: type,
    timestamp_ms: Date.now()
  };
  Object.keys(payload || {}).forEach(function (key) {
    event[key] = payload[key];
  });
  console.log(JSON.stringify(event));
  send(event);
}

function ptrString(value) {
  return value ? value.toString() : null;
}

function normalizeImplementation(implementation, module) {
  var rawOffset = module ? implementation.sub(module.base) : null;
  var isThumb = implementation.and(1).toInt32() === 1;
  var codeOffset = rawOffset;
  if (rawOffset && Process.arch === 'arm' && isThumb) {
    codeOffset = ptr(rawOffset).and(ptr('0xfffffffe'));
  }
  return {
    implementation: ptrString(implementation),
    module_name: module ? module.name : null,
    module_base: module ? ptrString(module.base) : null,
    raw_offset: rawOffset ? ptrString(rawOffset) : null,
    code_offset: codeOffset ? ptrString(codeOffset) : null,
    thumb: isThumb,
    arch: Process.arch
  };
}

function findRegisterNativesSymbols() {
  var libart = Process.findModuleByName('libart.so');
  if (!libart) return [];
  return Module.enumerateSymbolsSync('libart.so').filter(function (symbol) {
    return symbol.name.indexOf('RegisterNatives') !== -1 &&
      symbol.name.indexOf('CheckJNI') === -1;
  });
}

Java.perform(function () {
  var env = Java.vm.tryGetEnv();
  var candidates = findRegisterNativesSymbols();
  if (REGISTER_NATIVE_MAP_CONFIG.includeCandidates) {
    emit('register_natives_candidates', {
      count: candidates.length,
      names: candidates.map(function (item) { return item.name; })
    });
  }

  if (candidates.length === 0) {
    emit('error', { message: 'RegisterNatives symbol not found in libart.so' });
    return;
  }

  candidates.forEach(function (candidate) {
    emit('register_natives_hooked', {
      symbol: candidate.name,
      address: ptrString(candidate.address)
    });

    Interceptor.attach(candidate.address, {
      onEnter: function (args) {
        var className = null;
        try {
          className = env.getClassName(args[1]);
        } catch (error) {
          emit('register_natives_class_error', {
            symbol: candidate.name,
            error: String(error)
          });
          return;
        }

        if (!shouldKeepClass(className)) return;

        var methods = args[2];
        var count = args[3].toInt32();
        emit('register_natives_enter', {
          symbol: candidate.name,
          class_name: className,
          count: count,
          methods_ptr: ptrString(methods)
        });

        for (var index = 0; index < count; index++) {
          try {
            var row = methods.add(index * Process.pointerSize * 3);
            var name = row.readPointer().readCString();
            var signature = row.add(Process.pointerSize).readPointer().readCString();
            var implementation = row.add(Process.pointerSize * 2).readPointer();
            var module = Process.findModuleByAddress(implementation);
            var normalized = normalizeImplementation(implementation, module);
            emit('jni_mapping', Object.assign({
              source: 'RegisterNatives',
              symbol: candidate.name,
              class_name: className,
              method_name: name,
              signature: signature,
              index: index
            }, normalized));
          } catch (error) {
            emit('jni_mapping_error', {
              symbol: candidate.name,
              class_name: className,
              index: index,
              error: String(error)
            });
          }
        }
      }
    });
  });
});
