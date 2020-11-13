import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn import tree

class DecisionTree:
   
    dt=pd.read_csv('model/heart.csv')
    tdc = tree.DecisionTreeClassifier()
    
    def __init__(self):

    def train_model():
        
        from sklearn.model_selection import train_test_split
        # Choosing var target 
        y_target = dt['target'].values
        # Choosing params to help clasified
        x_features = dt[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']].values
        # Traning the model
        x_train,x_test,y_train,y_test = train_test_split(x_features,y_target, test_size = 0.3, random_state = 1)
        
        # Train Decision Tree Classifer
        tdc = tdc.fit(x_train,y_train)

        # Gettign accuracy
        y_pred = tdc.predict(x_test)
        print("Accuracy:",metrics.accuracy_score(y_test, y_pred))   

    def draw_tree():


    def classify_patient(self,patientInfo):
        return (f"Los datos de entrada:{patientInfo['age']},{patientInfo['sex']},{patientInfo['cp']},{patientInfo['trestbps']},{patientInfo['chol']},{patientInfo['fbs']},{patientInfo['restecg']},{patientInfo['thalach']},{patientInfo['exang']},{patientInfo['oldpeak']},{patientInfo['slope']},{patientInfo['ca']},{patientInfo['thal']}") 

