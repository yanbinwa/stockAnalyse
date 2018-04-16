# -*- coding: utf-8 -*- 
from django.http import HttpResponse
from .service import StockPredictServiceSingleton
import json
from django.views.decorators.csrf import csrf_exempt
# 
stockPredictService = StockPredictServiceSingleton();
stockPredictService.loadModel();

@csrf_exempt
def trainModel(request):
    bodyStr = request.body;
    body = json.loads(bodyStr);
    datas = body.get('datas');
    print datas;
    results = body.get('results');
    print results;
    ret = stockPredictService.trainModel(datas, results);
    return HttpResponse(json.dumps(ret));

@csrf_exempt
def predict(request):
    bodyStr = request.body;
    body = json.loads(bodyStr);
    data = body.get('data');
    ret = stockPredictService.predict(data);
    return HttpResponse(json.dumps(ret));