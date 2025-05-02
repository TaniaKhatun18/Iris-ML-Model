import joblib
import pandas as pd

Data = pd.read_csv("iris.csv")
def predict(data):
    clf = joblib.load("rf_model.sav")
    return clf.predict(Data)