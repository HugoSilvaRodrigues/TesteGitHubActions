import pandas as pd 
import os 
import sys 
import yaml
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
config_path=os.path.join(os.path.dirname(__file__),"config.yml")
def read():
    print("Lendo os dados:")
    with open(config_path, 'r') as file:
        config=yaml.safe_load(file)
    try:    
        data=pd.read_csv((config['data']['name']))
        print(data.head())
        print("Dados lidos")
        return data
    except Exception as e:
        print(e)
    
