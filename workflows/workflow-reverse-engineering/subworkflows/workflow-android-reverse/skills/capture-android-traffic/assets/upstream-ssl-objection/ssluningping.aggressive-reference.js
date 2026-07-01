/*
 * [LuoGe-Full-Unpinning]
 * 目标：覆盖 Java 层、系统底层、第三方库（OkHttp/Cronet）以及 WebView
 * instagram 绕过

 */

Java.perform(function () {
    const TAG = "[LuoGe-Expert]";
    const ArrayList = Java.use("java.util.ArrayList");

    // --- 1. 深度伪造 TrustManager (核心) ---
    const X509TrustManager = Java.use('javax.net.ssl.X509TrustManager');
    const TrustManager = Java.registerClass({
        name: 'com.luoge.unpinning.CustomTrustManager',
        implements: [X509TrustManager],
        methods: {
            checkClientTrusted(chain, authType) {},
            checkServerTrusted(chain, authType) {},
            getAcceptedIssuers() { return []; }
        }
    });
    const trustManagers = Java.array('javax.net.ssl.TrustManager', [TrustManager.$new()]);

    // --- 2. 覆盖系统级 SSLContext ---
    const SSLContext = Java.use('javax.net.ssl.SSLContext');
    SSLContext.init.overload('[Ljavax.net.ssl.KeyManager;', '[Ljavax.net.ssl.TrustManager;', 'java.security.SecureRandom').implementation = function (km, tm, sr) {
        console.log(TAG + " [SSLContext] 注入自定义 TrustManager");
        this.init(km, trustManagers, sr);
    };

    // --- 3. 针对 Android 10+ (Conscrypt) 底层拦截 ---
    try {
        const TrustManagerImpl = Java.use('com.android.org.conscrypt.TrustManagerImpl');
        // 绕过所有层级的递归校验
        TrustManagerImpl.checkTrustedRecursive.implementation = function () {
            return ArrayList.$new();
        };
        console.log(TAG + " [Conscrypt] 绕过底层递归校验");
    } catch (e) {}

    // --- 4. 彻底粉碎 OkHttp3 证书固定 (支持混淆类) ---
    try {
        const CertificatePinner = Java.use("okhttp3.CertificatePinner");
        CertificatePinner.check.overload('java.lang.String', 'java.util.List').implementation = function (host, list) {
            console.log(TAG + " [OkHttp3] 绕过 check: " + host);
        };
        CertificatePinner.findMatchingPins.implementation = function (host) {
            console.log(TAG + " [OkHttp3] 绕过 findMatchingPins: " + host);
            return ArrayList.$new();
        };
    } catch (e) {
        // 如果类名被混淆，这里可以根据方法签名动态枚举，目前先针对标准类名
    }

    // --- 5. 暴力绕过 Network Security Config ---
    try {
        const NetworkSecurityConfig = Java.use("android.security.net.config.NetworkSecurityConfig");
        NetworkSecurityConfig.isCleartextTrafficPermitted.overload().implementation = function () {
            return true;
        };
        // 强制所有域名使用默认（不校验）配置
        const DomainSpecificConfig = Java.use("android.security.net.config.DomainSpecificConfig");
        DomainSpecificConfig.hasCertificatePins.implementation = function () {
            return false;
        };
        console.log(TAG + " [NetConfig] 绕过域名固定配置");
    } catch (e) {}

    // --- 6. WebView 修正版 ---
    try {
        const WebViewClient = Java.use('android.webkit.WebViewClient');
        WebViewClient.onReceivedSslError.implementation = function (view, handler, error) {
            console.log(TAG + " [WebView] 强制执行 proceed()");
            handler.proceed();
        };
    } catch (e) {}

    // --- 7. HttpsURLConnection 域名校验绕过 ---
    try {
        const HttpsURLConnection = Java.use('javax.net.ssl.HttpsURLConnection');
        const HostnameVerifier = Java.use('javax.net.ssl.HostnameVerifier');
        const MyHostnameVerifier = Java.registerClass({
            name: 'com.luoge.unpinning.MyHostnameVerifier',
            implements: [HostnameVerifier],
            methods: {
                verify(hostname, session) { return true; }
            }
        });
        HttpsURLConnection.setDefaultHostnameVerifier(MyHostnameVerifier.$new());
    } catch (e) {}

    // --- 8. 针对 Google Cronet (很多大厂 App 在用) ---
    try {
        const CronetEngineBuilder = Java.use("org.chromium.net.CronetEngine$Builder");
        CronetEngineBuilder.enablePublicKeyPinningBypassForLocalTrustAnchors.implementation = function (arg) {
            return this.enablePublicKeyPinningBypassForLocalTrustAnchors(true);
        };
    } catch (e) {}

    console.log("\n" + TAG + " === 洛哥专用：全协议栈绕过已就绪 ===");
});

