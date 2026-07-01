package com.example.luov2;


import android.util.Log;

import com.example.luov2.handler.Ac1;
import com.example.luov2.handler.Ac2;
import com.example.luov2.handler.Learn;

import java.util.UUID;

import cn.iinti.sekiro3.business.api.SekiroClient;
import cn.iinti.sekiro3.business.api.interfaze.ActionHandler;
import cn.iinti.sekiro3.business.api.interfaze.SekiroRequest;
import cn.iinti.sekiro3.business.api.interfaze.SekiroResponse;
import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.callbacks.XC_LoadPackage;

public class hookRpc implements IXposedHookLoadPackage {

    private static final String TAG = "_luo";

    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam lpparam) throws Throwable {

        // 实现业务
        if (lpparam.processName.equals("22222222")) {// 请注意，一般sekiro只作用于特定的app
            Log.i(TAG, "packageName:" + "rpc启动" + lpparam.processName);
            new SekiroClient("test_xposed", UUID.randomUUID().toString(),"192.168.110.59",5612)
                    .setupSekiroRequestInitializer((sekiroRequest, handlerRegistry) ->
                            handlerRegistry.registerSekiroHandler(new ActionHandler() {
                                @Override
                                public String action() {
                                    return "testAction";
                                }

                                @Override
                                public void handleRequest(SekiroRequest sekiroRequest, SekiroResponse sekiroResponse) {
                                    sekiroResponse.success("ok hello kity");// 接口处理逻辑，我们不做任何处理，直接返回字符串：ok
                                }
                            })
                    ).start();
        }


        if (lpparam.processName.equals(lpparam.packageName)){
            Log.i(TAG, "handleLoadPackage: RPC " + lpparam.packageName);
            new SekiroClient("xl", UUID.randomUUID().toString(),"192.168.110.59",5612)
                    .setupSekiroRequestInitializer((sekiroRequest, handlerRegistry) ->
                            {
                                handlerRegistry.registerSekiroHandler(new Ac1()); // 接口1 登录
                                handlerRegistry.registerSekiroHandler(new Ac2()); // 接口2 注册
                                handlerRegistry.registerSekiroHandler(new Learn(lpparam.classLoader)); // 接口2 注册
//                                handlerRegistry.registerSekiroHandler(new Ac2()); // 接口2 注册
//                                handlerRegistry.registerSekiroHandler(new Ac2()); // 接口2 注册
//                                handlerRegistry.registerSekiroHandler(new Ac2()); // 接口2 注册
//                                handlerRegistry.registerSekiroHandler(new Ac2()); // 接口2 注册
                            }

                    ).start();

        };

    }
}
