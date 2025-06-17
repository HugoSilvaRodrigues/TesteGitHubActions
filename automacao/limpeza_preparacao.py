import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
import sys 
import os
import yaml
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
config_path=os.path.join(os.path.dirname(__file__),"config.yml")
with open(config_path, "r") as file:
    config=yaml.safe_load(file)

def preprocessing(data):
    print("Iniciando limpeza dos dados:")
    data["high_traffic"]=data["high_traffic"].fillna(value="low")
    data.dropna(inplace=True)
    data.replace(["High","low"],["1","0"],inplace=True)
    data["high_traffic"]=data["high_traffic"].astype('int')
    data.drop(['recipe'],axis=1,inplace=True)
    data['servings']=data['servings'].str.strip("as a snack").astype('int')
    X=data.drop(['high_traffic'],axis=1)
    y=data['high_traffic']
    print("Iniciando pre processamento dos dados")
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=config['training']['test_size'])
    pipeline=joblib.load(config['data']['pipeline'])
    X_train=pipeline.transform(X_train)
    X_test=pipeline.transform(X_test)
    return X_train,X_test,y_train,y_test