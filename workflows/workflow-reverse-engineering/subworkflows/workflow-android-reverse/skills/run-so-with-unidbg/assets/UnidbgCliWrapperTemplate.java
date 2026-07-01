package task.unidbg;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.Module;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.AbstractJni;
import com.github.unidbg.linux.android.dvm.DalvikModule;
import com.github.unidbg.linux.android.dvm.DvmClass;
import com.github.unidbg.linux.android.dvm.StringObject;
import com.github.unidbg.linux.android.dvm.VM;
import com.github.unidbg.memory.Memory;

import java.io.File;

/**
 * Minimal Unidbg CLI wrapper template.
 *
 * Copy this file into a TASK-local Unidbg project and replace the constants.
 * The last stdout line must be the business result so Python callers can parse
 * it without depending on verbose Unidbg logs.
 */
public class UnidbgCliWrapperTemplate extends AbstractJni {

    private static final boolean IS_64_BIT = true;
    private static final int ANDROID_API = 23;
    private static final String PROCESS_NAME = "replace.with.package";
    private static final String APK_PATH = "inputs/app.apk"; // optional; use createDalvikVM() if not needed.
    private static final String SO_PATH = "inputs/libtarget.so";
    private static final String JNI_CLASS = "replace/with/NativeClass";
    private static final String JNI_METHOD = "target(Ljava/lang/String;)Ljava/lang/String;";

    private final AndroidEmulator emulator;
    private final VM vm;
    private final DvmClass targetClass;
    @SuppressWarnings("unused")
    private final Module module;

    public UnidbgCliWrapperTemplate() {
        emulator = (IS_64_BIT ? AndroidEmulatorBuilder.for64Bit() : AndroidEmulatorBuilder.for32Bit())
                .setProcessName(PROCESS_NAME)
                .build();
        Memory memory = emulator.getMemory();
        memory.setLibraryResolver(new AndroidResolver(ANDROID_API));

        File apk = new File(APK_PATH);
        vm = apk.exists() ? emulator.createDalvikVM(apk) : emulator.createDalvikVM();
        vm.setVerbose(false);
        vm.setJni(this);

        DalvikModule dm = vm.loadLibrary(new File(SO_PATH), false);
        dm.callJNI_OnLoad(emulator);
        module = dm.getModule();
        targetClass = vm.resolveClass(JNI_CLASS);
    }

    public String call(String input) {
        StringObject result = targetClass.callStaticJniMethodObject(
                emulator,
                JNI_METHOD,
                new StringObject(vm, input)
        );
        return result == null ? "" : result.getValue();
    }

    public void close() {
        emulator.close();
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("usage: java ... UnidbgCliWrapperTemplate '<input>'");
            System.exit(2);
        }
        UnidbgCliWrapperTemplate wrapper = new UnidbgCliWrapperTemplate();
        try {
            String result = wrapper.call(args[0]);
            System.out.println(result);
        } finally {
            wrapper.close();
        }
    }
}
