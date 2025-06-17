from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import os
import sys
import yaml
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

with open('config.yml','r') as file:
    config=yaml.safe_load(file)
    
def train_model(X_train,X_test,y_train,y_test):
    print("Iniciando treinamento do modelo")
    rfc=RandomForestClassifier(n_estimators=config['model']['params']['n_estimators'], criterion=config['model']['params']['criterion'],
                               max_leaf_nodes=config['model']['params']['max_leaf_nodes'], max_depth=config['model']['params']['max_depth'])
    rfc.fit(X_train,y_train)
    y_predict=rfc.predict(X_test)
    score=f1_score(y_test,y_predict)
    if score>=config['model']['best_score']:
        print("Treinamento realizado com sucesso")
        return rfc, score
    else:
        print("Modelo não teve a perfomance esperada")
        return None,None