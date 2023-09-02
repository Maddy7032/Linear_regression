"""
created on sep 02 2023
author: md shoaib
"""

import numpy as np
import pandas as pd
import pickle
from flask import Flask, request

# model.pkl is used to run prediction on new data

app=Flask(__name__)
pickle_in = open("model.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route("/")
def welcome():
    return "welcome ALL"

@app.route("/predict", methods=["Get"])
def predict_note_aithontication():
    input_cols =   ['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))



    prediction = classifier.predict([list1])
    #prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello the answer is"+str(prediction)

@app.route("/predict_file", methods=["Post"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return str(list(prediction))
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)