package com.example.luov2.handler;

import cn.iinti.sekiro3.business.api.interfaze.Action;
import cn.iinti.sekiro3.business.api.interfaze.RequestHandler;
import cn.iinti.sekiro3.business.api.interfaze.SekiroRequest;
import cn.iinti.sekiro3.business.api.interfaze.SekiroResponse;

@Action("a22") // 注册接口
public class Ac2 implements RequestHandler{

    @Override
    public void handleRequest(SekiroRequest sekiroRequest, SekiroResponse sekiroResponse) {

        // sekiroRequest 接受外部传参
        // 调用hook fun  继续调用 拿到返回值  主动调用
        sekiroResponse.success("hello world2");

    }
}
