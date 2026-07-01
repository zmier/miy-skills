'use strict';

const TARGET_CLASS = '__TARGET_CLASS__';

function emit(event, payload) {
  send(Object.assign({ event: event, timestamp: Date.now() }, payload || {}));
}

function findRegisterNatives() {
  return Module.enumerateSymbolsSync('libart.so').filter(function (symbol) {
    return symbol.name.indexOf('RegisterNatives') !== -1 &&
      symbol.name.indexOf('CheckJNI') === -1;
  });
}

Java.perform(function () {
  const candidates = findRegisterNatives();
  emit('register-natives-candidates', {
    count: candidates.length,
    names: candidates.map(function (item) { return item.name; })
  });
  if (candidates.length === 0) {
    emit('error', { message: 'RegisterNatives symbol not found' });
    return;
  }

  const address = candidates[0].address;
  emit('register-natives-hooked', { address: address.toString() });

  Interceptor.attach(address, {
    onEnter: function (args) {
      let className;
      try {
        className = Java.vm.tryGetEnv().getClassName(args[1]);
      } catch (error) {
        return;
      }
      if (className !== TARGET_CLASS) {
        return;
      }

      const methods = args[2];
      const count = args[3].toInt32();
      for (let index = 0; index < count; index++) {
        const row = methods.add(index * Process.pointerSize * 3);
        const name = row.readPointer().readCString();
        const signature = row.add(Process.pointerSize).readPointer().readCString();
        const implementation = row.add(Process.pointerSize * 2).readPointer();
        const module = Process.findModuleByAddress(implementation);
        emit('jni-mapping', {
          class_name: className,
          method_name: name,
          signature: signature,
          implementation: implementation.toString(),
          module_name: module ? module.name : null,
          module_base: module ? module.base.toString() : null,
          offset: module ? implementation.sub(module.base).toString() : null,
          thumb: implementation.and(1).toInt32() === 1
        });
      }
    }
  });
});
