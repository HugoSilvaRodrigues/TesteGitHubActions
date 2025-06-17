from read_files import read
from limpeza_preparacao import preprocessing
from ml_model import train_model
from save_model import save_model
data=read()
X_train,X_test,y_train,y_test=preprocessing(data)
model,score=train_model(X_train,X_test,y_train,y_test)
if model!=None:
    save_model(model)