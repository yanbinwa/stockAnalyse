# -*- coding: utf-8 -*- 
import numpy as np
from sklearn.svm import SVC
from config import Config
import constants as Constants
import pickle
import os

config = Config();

MODEL_FILE = config.getProperties(Constants.MODEL_FILE_KEY);

class StockPredictServiceSingleton:
    __instance = None
    
    def __init__(self):
        return;
        
    def __new__(cls, *args, **kwd):
        if StockPredictServiceSingleton.__instance is None:
            StockPredictServiceSingleton.__instance = object.__new__(cls, *args, **kwd)
        return StockPredictServiceSingleton.__instance;
    
    def loadModel(self):
        if not os.path.exists(MODEL_FILE):
            return;
        with open(MODEL_FILE, 'rb') as f:
            (self.model) = pickle.load(f);
        return;
    
    def storeModel(self):
        if self.model == None:
            return;
        self.deleteFile(MODEL_FILE);
        with open(MODEL_FILE, 'wb') as f:
            pickle.dump((self.model), f);
        return;
    
    #输入是训练的股票价格趋势，以及是否是增长幅度较大的股票，这里进行训练模型，并且加载模型
    def trainModel(self, datas, results):
        x = np.array(datas);
        y = np.array(results);
        self.model = SVC();
        self.model.fit(x, y);
        self.storeModel();
        return "train model success";
    
    #输入是一段时间的股票价格，输出是判断这个股票的涨幅
    def predict(self, data):
        ret = self.model.predict(data);
        if ret is None or len(ret) == 0:
            return "predict fail";
        return ret[0];
    
    def deleteFile(self, fileName):
        if os.path.isfile(fileName):
            os.remove(fileName);