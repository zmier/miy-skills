package your.module.package;

import cn.iinti.sekiro3.business.api.interfaze.Action;
import cn.iinti.sekiro3.business.api.interfaze.RequestHandler;
import cn.iinti.sekiro3.business.api.interfaze.SekiroRequest;
import cn.iinti.sekiro3.business.api.interfaze.SekiroResponse;
import de.robv.android.xposed.XposedHelpers;

@Action("safeActionName")
public class SekiroActionHandlerTemplate implements RequestHandler {
    private static final String OPERATION_TYPE = "com.example.safe.operation";
    private final ClassLoader targetClassLoader;

    public SekiroActionHandlerTemplate(ClassLoader classLoader) {
        this.targetClassLoader = classLoader;
    }

    @Override
    public void handleRequest(SekiroRequest request, SekiroResponse response) {
        String arg1 = sanitize(request.getString("arg1"));
        String arg2 = sanitize(request.getString("arg2"));
        boolean real = "1".equals(request.getString("real"));
        boolean includeRaw = "1".equals(request.getString("includeRaw"));

        if (!real) {
            response.success("{"
                    + "\"ok\":true,"
                    + "\"dryRun\":true,"
                    + "\"allowlistOnly\":true,"
                    + "\"businessRpcTriggered\":false,"
                    + "\"sensitiveHeadersReturned\":false,"
                    + "\"operationType\":\"" + json(OPERATION_TYPE) + "\""
                    + "}");
            return;
        }

        try {
            Class<?> targetClass = XposedHelpers.findClass("com.example.TargetClass", targetClassLoader);
            Object result = XposedHelpers.callStaticMethod(targetClass, "targetMethod", arg1, arg2);

            boolean businessOk = isBusinessSuccess(result);
            response.success("{"
                    + "\"ok\":" + businessOk + ","
                    + "\"dryRun\":false,"
                    + "\"allowlistOnly\":true,"
                    + "\"businessRpcTriggered\":true,"
                    + "\"sensitiveHeadersReturned\":false,"
                    + "\"operationType\":\"" + json(OPERATION_TYPE) + "\","
                    + "\"transportOk\":true,"
                    + "\"businessOk\":" + businessOk + ","
                    + "\"result\":\"" + json(summarize(result, includeRaw)) + "\""
                    + "}");
        } catch (Throwable throwable) {
            response.success("{"
                    + "\"ok\":false,"
                    + "\"dryRun\":false,"
                    + "\"allowlistOnly\":true,"
                    + "\"businessRpcTriggered\":true,"
                    + "\"sensitiveHeadersReturned\":false,"
                    + "\"operationType\":\"" + json(OPERATION_TYPE) + "\","
                    + "\"transportOk\":false,"
                    + "\"businessOk\":false,"
                    + "\"errorType\":\"" + json(throwable.getClass().getSimpleName()) + "\","
                    + "\"errorMessage\":\"" + json(sanitize(String.valueOf(throwable.getMessage()))) + "\""
                    + "}");
        }
    }

    private static boolean isBusinessSuccess(Object result) {
        String text = String.valueOf(result);
        return text.contains("\"success\":true")
                || text.contains("\"resultCode\":\"SUCCESS\"")
                || text.contains("\"resultDesc\":\"SUCCESS\"");
    }

    private static String summarize(Object result, boolean includeRaw) {
        String text = String.valueOf(result);
        if (includeRaw) {
            return sanitize(text);
        }
        return text.length() > 160 ? text.substring(0, 160) : text;
    }

    private static String sanitize(String value) {
        if (value == null) {
            return "";
        }
        String stripped = value.replaceAll("[\\r\\n\\t]", " ").trim();
        return stripped.length() > 512 ? stripped.substring(0, 512) : stripped;
    }

    private static String json(String value) {
        return sanitize(value)
                .replace("\\", "\\\\")
                .replace("\"", "\\\"");
    }
}
