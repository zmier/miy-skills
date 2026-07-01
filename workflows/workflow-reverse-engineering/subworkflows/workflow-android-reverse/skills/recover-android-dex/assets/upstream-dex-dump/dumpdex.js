/**
 * 洛哥魔改兼容版
 */

function dump_dex_hybrid() {
    console.log("[*] 正在使用模糊匹配逻辑寻找 Hook 点...");

    var libart = Process.findModuleByName("libart.so");
    if (!libart) return;

    var addr_DefineClass = null;
    var symbols = libart.enumerateSymbols();

    // 沿用你之前跑通的模糊匹配过滤
    for (var i = 0; i < symbols.length; i++) {
        var name = symbols[i].name;
        if (name.indexOf("ClassLinker") >= 0 &&
            name.indexOf("DefineClass") >= 0 &&
            name.indexOf("DexFile") >= 0) {

            addr_DefineClass = symbols[i].address;
            console.log("[+] 锁定有效 Hook 点: " + name);
            break;
        }
    }

    if (!addr_DefineClass) {
        console.log("[-] 模糊匹配也失败了，尝试强制搜索 DefineClass 关键字...");
        // 最后的挣扎：只搜 DefineClass
        addr_DefineClass = Module.findExportByName("libart.so", "_ZN3art11ClassLinker11DefineClassEPNS_6ThreadEPKcmNS_6HandleINS_6mirror11ClassLoaderEEERKNS_7DexFileERKNS_3dex8ClassDefE");
    }

    if (addr_DefineClass) {
        var dex_maps = {};
        Interceptor.attach(addr_DefineClass, {
            onEnter: function(args) {
                // 核心增强：尝试从 args[5] 或 args[4] 获取 DexFile 指针
                // 东软这种包建议遍历一下
                for (var arg_idx = 4; arg_idx <= 6; arg_idx++) {
                    try {
                        var dex_file_ptr = args[arg_idx];
                        // 从 DexFile 对象偏移读取 Begin (base) 和 Size
                        var base = ptr(dex_file_ptr).add(Process.pointerSize).readPointer();
                        var size = ptr(dex_file_ptr).add(Process.pointerSize * 2).readUInt();

                        if (size > 1024 * 512) { // 过滤掉 512KB 以下的
                            var key = base + "_" + size;
                            if (!dex_maps[key]) {
                                dex_maps[key] = true;

                                // 强制检查 Magic
                                Memory.protect(base, size, 'rwx');
                                var magic = Memory.readUtf8String(base, 4);

                                if (magic.indexOf("dex") === 0) {
                                    console.log("[√] 捕获 DEX! Addr: " + base + " | Size: " + size);
                                    save_to_files(base, size);
                                }
                            }
                        }
                    } catch (e) {}
                }
            }
        });
    }
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
function save_to_files(base, size) {
    // var pkg = "com.neusoft.sysucc.app.patient";
    var pkg = getPackageName();
    var path = "/data/data/" + pkg + "/files/" + base + ".dex";
    try {
        var buffer = Memory.readByteArray(base, size);
        var f = new File(path, "wb");
        f.write(buffer);
        f.flush();
        f.close();
        console.log("    已保存至: " + path);
    } catch (e) {
        console.log("    保存失败: " + e.message);
    }
}

setImmediate(dump_dex_hybrid);