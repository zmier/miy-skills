package com.example.luov2.handler;

import android.util.Log;

import cn.iinti.sekiro3.business.api.interfaze.Action;
import cn.iinti.sekiro3.business.api.interfaze.RequestHandler;
import cn.iinti.sekiro3.business.api.interfaze.SekiroRequest;
import cn.iinti.sekiro3.business.api.interfaze.SekiroResponse;
import de.robv.android.xposed.XposedHelpers;

@Action("learn")
public class Learn implements RequestHandler {

    private static final String TAG = "_luo";
    public final ClassLoader mycls;

    public Learn(ClassLoader classLoader){
        mycls = classLoader;
    }



    @Override
    public void handleRequest(SekiroRequest sekiroRequest, SekiroResponse sekiroResponse) {

        // hook 逻辑
        Log.i(TAG, "handleRequest: success");
        // 提取外部参数
        String a1 = sekiroRequest.getString("arg1");
        String a2 = sekiroRequest.getString("arg2");
        Log.i(TAG, "handleRequesta1: " + a1);
        Log.i(TAG, "handleRequesta2: " + a2);
        // 获取lei 方法
        Class<?> MD5cls = XposedHelpers.findClass("cn.thecover.lib.common.manager.SignManager", this.mycls);
        Object md5_1 = XposedHelpers.callStaticMethod(MD5cls, "getSign", a1,"",a2);
//        Log.i(TAG, "handleRequest: " + md5_1);
        sekiroResponse.success(md5_1);

    }
}
