import os 
import sys
import joblib
import yaml
import json

config_path=os.path.join(os.path.dirname(__file__),"config.yml")
with open(config_path,'r') as file:
    config=yaml.safe_load(file)

def save_model(model):
    print("Salvando o modelo")
    os.makedirs(config['saving']['folder_name'],exist_ok=True)
    files=os.listdir(config['saving']['folder_name'])
    if len(files)==0:
        os.makedirs(config['saving']['folder_name']+"\model_1")
        joblib.dump(model,config['saving']['folder_name']+"\model_1\model_1.pkl")
        with open (config['saving']['folder_name']+"\model_1\params.csv","w") as params:
            params.write(json.dumps(config['model']['params']))
    else:
        most_recent=str(int(files[len(files)-1][6:])+1)
        os.makedirs(config['saving']['folder_name']+"\model_"+most_recent)
        joblib.dump(model,config['saving']['folder_name']+"\model_"+most_recent+"\model_"+most_recent+".pkl")
        with open (config['saving']['folder_name']+"\model_"+most_recent+"\params.csv","w") as params:
            params.write(json.dumps(config['model']['params']))
    print("Modelo Salvo")
    