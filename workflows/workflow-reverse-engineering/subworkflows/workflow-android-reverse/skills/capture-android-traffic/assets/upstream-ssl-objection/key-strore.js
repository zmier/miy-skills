

// 在https双向认证的情况下，dump客户端证书为p12. 证书密码: hooker
var password = "hooker";

function getNowTime() {
    var date = new Date();
    var fmt = "YYYY_mm_dd_HH_MM_SS";
    const opt = {
        "Y+": date.getFullYear().toString(),
        "m+": (date.getMonth() + 1).toString(),
        "d+": date.getDate().toString(),
        "H+": date.getHours().toString(),
        "M+": date.getMinutes().toString(),
        "S+": date.getSeconds().toString()
    };
    for (let k in opt) {
        let ret = new RegExp("(" + k + ")").exec(fmt);
        if (ret) {
            fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")));
        }
    }
    return fmt + "_" + Math.floor(Math.random() * 100);
}

function getPackageName() {
    var packageName = null;
    try {
        // 优先使用 Frida 内置的 context 接口，这是最稳妥的
        packageName = Java.androidContext.getPackageName();
    } catch (e) {
        try {
            var ActivityThread = Java.use('android.app.ActivityThread');
            packageName = ActivityThread.currentPackageName();
            if (!packageName) {
                var app = ActivityThread.currentApplication();
                if (app) packageName = app.getPackageName();
            }
        } catch (e2) {
            packageName = "unknown";
        }
    }
    return packageName;
}

function dump2sdcard(pri, cert, filePath) {
    try {
        var KeyStore = Java.use("java.security.KeyStore");
        var X509Certificate = Java.use("java.security.cert.X509Certificate");
        var FileOutputStream = Java.use("java.io.FileOutputStream");
        var StringClass = Java.use('java.lang.String');

        console.log("[*] 正在导出证书至: " + filePath);

        // 处理证书链：如果是单个证书，转为数组
        var chain;
        if (cert.$className === '[Ljava.security.cert.Certificate;') {
            chain = cert;
        } else {
            var castCert = Java.cast(cert, X509Certificate);
            chain = Java.array("java.security.cert.Certificate", [castCert]);
        }

        // 实例化 PKCS12 (尝试不加 "BC" 以提高兼容性)
        var ks = KeyStore.getInstance("PKCS12");
        ks.load(null, null);

        var passChars = StringClass.$new(password).toCharArray();
        ks.setKeyEntry("client", pri, passChars, chain);

        var out = FileOutputStream.$new(filePath);
        ks.store(out, passChars);
        out.close();
        console.log("[+] 导出成功!");
    } catch (error) {
        console.log("[!] 导出失败: " + error);
    }
}

function main() {
    Java.perform(function() {
        var packageName = getPackageName();
        // 建议路径改为 files 目录，避免根目录权限问题
        var baseDir = "/data/data/" + packageName + "/files/";

        console.log("[*] 监听双向认证证书导出...");
        console.log("[*] 预设存储路径: " + baseDir);

        var PrivateKeyEntry = Java.use("java.security.KeyStore$PrivateKeyEntry");

        // Hook getPrivateKey
        PrivateKeyEntry.getPrivateKey.implementation = function() {
            var result = this.getPrivateKey(); // 获取原始私钥
            var cert = this.getCertificate();  // 获取关联证书

            var path = baseDir + "client_dump_" + getNowTime() + ".p12";
            dump2sdcard(result, cert, path);

            return result;
        };

        // Hook getCertificateChain (双向认证通常会触发此方法)
        PrivateKeyEntry.getCertificateChain.implementation = function() {
            var result = this.getCertificateChain();
            var priKey = this.getPrivateKey();

            var path = baseDir + "chain_dump_" + getNowTime() + ".p12";
            // 这里 result 本身就是 chain 数组
            dump2sdcard(priKey, result, path);

            return result;
        };
    });
}

setImmediate(main);
