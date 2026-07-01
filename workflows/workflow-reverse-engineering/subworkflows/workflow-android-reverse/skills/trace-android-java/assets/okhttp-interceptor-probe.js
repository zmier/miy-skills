Java.perform(function () {
  var Builder = Java.use("okhttp3.OkHttpClient$Builder");

  function event(kind, payload) {
    console.log(JSON.stringify(Object.assign({
      kind: kind,
      ts: Date.now()
    }, payload)));
  }

  Builder.addInterceptor.implementation = function (interceptor) {
    var className = interceptor ? interceptor.getClass().getName().toString() : "null";
    event("okhttp_add_interceptor", { className: className });
    return this.addInterceptor(interceptor);
  };

  Builder.addNetworkInterceptor.implementation = function (interceptor) {
    var className = interceptor ? interceptor.getClass().getName().toString() : "null";
    event("okhttp_add_network_interceptor", { className: className });
    return this.addNetworkInterceptor(interceptor);
  };
});
