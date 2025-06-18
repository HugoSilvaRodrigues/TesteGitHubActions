import streamlit as st 
import joblib
import pandas as pd
import os


def load_model_from_folder():
    models=os.listdir("automacao/models")
    if len(models)==0:
        print("Nenhum modelo treinado")
    else:
        models=[models[i].replace("model_","") for i in range(len(models))]
        models.sort(reverse=True)
        path="automacao/models/model_"+models[0]+"/model_"+models[0]+".pkl"
        model=joblib.load(path)
        return model
    
def load_model_single():
    model=joblib.load("final_model.pkl")
    return model
        
form = st.form("my_form")
with form:
    col1, col2 = st.columns(2)
    with col1:
        print(os.path.dirname("."))
        calories = st.number_input("Calories: ")
        carboidrato = st.number_input("Carbohydrate: ")
        sugar = st.number_input("Sugar: ") 
    with col2:
        protein = st.number_input("Protein: ")
        servings = st.number_input("Servings: ")
        category = st.selectbox("What is the category: ",
                                ("Potato",
                                 "Breakfast",
                                 "Beverages",
                                 "One Dish Meal",
                                 "Chicken Breast",
                                 "Lunch/Snacks",
                                 "Pork",
                                 "Chicken",
                                 "Vegetable",
                                 "Meat",
                                 "Dessert"))
    if form.form_submit_button("Submit"):
        pipeline=joblib.load("pipeline.pkl")
        data=pd.DataFrame({"calories":[calories],"carbohydrate":[carboidrato],"sugar":[sugar],"protein":[protein],"servings":[servings],"category":[category]})
        data_formated=pipeline.transform(data)
        model=load_model_single()
        try:
            predict=model.predict(data_formated)
            if predict==1:
                st.write("High traffic")
            else:
                st.write("Low traffic")
        except Exception as e:
            print(e)
        