package com.example.luov2.handler;


import android.util.Log;

import cn.iinti.sekiro3.business.api.interfaze.Action;
import cn.iinti.sekiro3.business.api.interfaze.RequestHandler;
import cn.iinti.sekiro3.business.api.interfaze.SekiroRequest;
import cn.iinti.sekiro3.business.api.interfaze.SekiroResponse;

@Action("a11")
public class Ac1 implements RequestHandler{
    private static final String TAG = "_luo";

    @Override
    public void handleRequest(SekiroRequest sekiroRequest, SekiroResponse sekiroResponse) {

        Log.i(TAG, "handleRequest: " + "hook success");
         sekiroResponse.success("hello world1");

    }
}
