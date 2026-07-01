'use strict';

const CONFIG = __CONFIG_JSON__;
let sequence = 0;

function emit(event, payload) {
  send(Object.assign({
    event: event,
    timestamp: Date.now(),
    sequence: sequence++
  }, payload || {}));
}

function toHex(buffer) {
  return Array.prototype.map.call(new Uint8Array(buffer), function (value) {
    return ('0' + value.toString(16)).slice(-2);
  }).join('');
}

function install() {
  const module = Process.findModuleByName(CONFIG.module);
  if (module === null) {
    return false;
  }

  let address = module.base.add(ptr(CONFIG.offset));
  if (CONFIG.thumb) {
    address = address.or(1);
  }
  emit('native-hook', {
    module_name: module.name,
    module_base: module.base.toString(),
    hook_address: address.toString(),
    offset: CONFIG.offset,
    thumb: CONFIG.thumb
  });

  Interceptor.attach(address, {
    onEnter: function (args) {
      const callerOffset = this.returnAddress
        .and(ptr(Process.pointerSize === 4 ? '0xfffffffe' : '0xffffffffffffffff'))
        .sub(module.base);
      const caller = callerOffset.toString();
      if (CONFIG.caller_offsets.length > 0 &&
          CONFIG.caller_offsets.indexOf(caller) === -1) {
        return;
      }

      const pointer = args[CONFIG.buffer_arg];
      const requested = args[CONFIG.length_arg].toInt32();
      const length = Math.min(Math.max(requested, 0), CONFIG.max_bytes);
      try {
        const bytes = pointer.readByteArray(length);
        let text = null;
        try {
          text = pointer.readUtf8String(length);
        } catch (error) {
          text = null;
        }
        emit('native-buffer', {
          caller_offset: caller,
          requested_length: requested,
          captured_length: length,
          text: text,
          hex: toHex(bytes)
        });
      } catch (error) {
        emit('read-error', {
          caller_offset: caller,
          requested_length: requested,
          message: String(error)
        });
      }
    }
  });
  return true;
}

const timer = setInterval(function () {
  if (install()) {
    clearInterval(timer);
  }
}, 100);
