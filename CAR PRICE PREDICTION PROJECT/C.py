from flask import Flask,redirect,url_for,render_template,request
import pandas as pd
import sklearn

print(sklearn.__version__)

import numpy as np
import pickle


app = Flask(__name__, static_url_path='/static')
Model= pickle.load(open("templates/C.pkl",'rb'))

data=pd.read_csv('templates/Clean.csv')

@app.route('/')
def hello_world():
    companies = sorted(data['Company'].unique())
    car_models=sorted(data['Model'].unique())
    years=sorted(data['year'].unique())
    fuel_type=(data['Fuel'].unique())
    Km_Driven=(data['Km_Driven'] )
    gear=(data['Gear'].unique())
    #companies.insert(0,"Select Company")
    

    return render_template("WEB.html",companies=companies,car_models=car_models,years=years,fuel_type=fuel_type,gear=gear)



@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get('car_model')
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    KM_Driven=int(request.form.get('KM_Driven'))
    Gear=request.form.get('Gear')
    print(company,car_model,year,fuel_type,KM_Driven,Gear)

    prediction=Model.predict(pd.DataFrame([[company,car_model,year,fuel_type,KM_Driven,Gear]],columns=['Company','Model','year','Fuel','Km_Driven','Gear']))
    
    return  str(abs(np.round(prediction[0],2)))



if __name__ == '__main__':
    app.run(debug=True)