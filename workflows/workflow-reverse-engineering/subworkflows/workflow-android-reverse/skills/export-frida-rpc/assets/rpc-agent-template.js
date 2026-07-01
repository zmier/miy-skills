'use strict';

var RPC_AGENT_CONFIG = {
  schema: 'android.frida_rpc.v1',
  name: 'rpc-agent-template',
  targetClass: 'REPLACE_WITH_TARGET_CLASS',
  targetMethod: 'REPLACE_WITH_TARGET_METHOD'
};

function ok(value, meta) {
  return {
    ok: true,
    schema: RPC_AGENT_CONFIG.schema,
    value: value,
    meta: meta || {}
  };
}

function fail(error) {
  return {
    ok: false,
    schema: RPC_AGENT_CONFIG.schema,
    error: String(error),
    stack: error && error.stack ? String(error.stack) : null
  };
}

rpc.exports = {
  compute: function (input) {
    return new Promise(function (resolve, reject) {
      Java.perform(function () {
        try {
          // TASK 中替换为真实类、重载和类型桥接。
          // var Target = Java.use(RPC_AGENT_CONFIG.targetClass);
          // var result = Target[RPC_AGENT_CONFIG.targetMethod](String(input.value));
          // resolve(ok(String(result), { target_class: RPC_AGENT_CONFIG.targetClass }));
          resolve(ok(input, { template: true }));
        } catch (error) {
          resolve(fail(error));
        }
      });
    });
  },

  ping: function () {
    return {
      ok: true,
      schema: RPC_AGENT_CONFIG.schema,
      agent: RPC_AGENT_CONFIG.name
    };
  }
};
