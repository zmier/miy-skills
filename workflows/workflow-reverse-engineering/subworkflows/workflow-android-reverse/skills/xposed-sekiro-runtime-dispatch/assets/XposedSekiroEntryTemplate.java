package your.module.package;

import android.util.Log;

import java.util.UUID;

import cn.iinti.sekiro3.business.api.SekiroClient;
import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.callbacks.XC_LoadPackage;

public class XposedSekiroEntryTemplate implements IXposedHookLoadPackage {
    private static final String TAG = "r4x-sekiro";

    private static final String TARGET_PACKAGE = "com.example.target";
    private static final String TARGET_PROCESS = "com.example.target";
    private static final String GROUP = "task_group";
    private static final String SERVER_HOST = "127.0.0.1";
    private static final int SERVER_PORT = 5612;

    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam lpparam) throws Throwable {
        if (!TARGET_PACKAGE.equals(lpparam.packageName)) {
            return;
        }
        Log.i(TAG, "module-loaded package=" + lpparam.packageName
                + " process=" + lpparam.processName);
        Log.i(TAG, "classloader-ready process=" + lpparam.processName
                + " classLoader=" + lpparam.classLoader.getClass().getName());

        if (!TARGET_PROCESS.equals(lpparam.processName)) {
            Log.i(TAG, "action-server-skip process=" + lpparam.processName
                    + " reason=not-target-process");
            return;
        }

        new SekiroClient(GROUP, UUID.randomUUID().toString(), SERVER_HOST, SERVER_PORT)
                .setupSekiroRequestInitializer((request, registry) -> {
                    registry.registerSekiroHandler(new SekiroActionHandlerTemplate(lpparam.classLoader));
                })
                .start();
    }
}
