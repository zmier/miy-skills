Java.perform(function () {
  function text(value) {
    return value === null || value === undefined ? null : String(value);
  }

  function readStaticField(className, fieldName) {
    const clazz = Java.use(className).class;
    const field = clazz.getDeclaredField(fieldName);
    field.setAccessible(true);
    return field.get(null);
  }

  const result = {
    jadx_display_name: "<JADX_DISPLAY_NAME>",
    runtime_class_name: null,
    interface_or_declared_type: "<DECLARED_TYPE>",
    method_signature: "<METHOD_SIGNATURE>",
    inputs: {},
    output: null,
  };

  // 方式一：JADX 存在 `renamed from` 时，填写 Dex 真实类名。
  const RuntimeClass = Java.use("<RUNTIME_CLASS_NAME>");
  result.runtime_class_name = text(RuntimeClass.class.getName());

  // 方式二：接口实现保存在字段中时，用反射读取真实对象类型。
  // const impl = readStaticField("<OWNER_CLASS>", "<FIELD_NAME>");
  // result.runtime_class_name = text(impl.getClass().getName());

  // 只读取本 TASK 所需的最小输入和输出，不做全局枚举。
  // result.inputs.example = text(RuntimeClass.someInput());
  // result.output = text(RuntimeClass.targetMethod());

  send({
    type: "runtime-symbol-probe",
    data: result,
  });
});
