import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


class DecisionTree:
   
    dt=pd.read_csv('model/heart.csv')
    def __init__(self):
        print("Entro")

    def train_model():
        from sklearn import tree
        from sklearn.model_selection import train_test_split

        print

    def classify_patient(self,patientInfo):
        return (f"Los datos de entrada:{patientInfo['age']},{patientInfo['sex']},{patientInfo['cp']},{patientInfo['trestbps']},{patientInfo['chol']},{patientInfo['fbs']},{patientInfo['restecg']},{patientInfo['thalach']},{patientInfo['exang']},{patientInfo['oldpeak']},{patientInfo['slope']},{patientInfo['ca']},{patientInfo['thal']}") 

