import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn import tree



class DecisionTree:

    
    def __init__(self):
        self.tdc = tree.DecisionTreeClassifier()
        self.dt = pd.read_csv('data/heart.csv')

    def train_model(self):
        from sklearn.model_selection import train_test_split
        # Choosing var target 
        y_target = self.dt['target'].values
        # Choosing params to help clasified
        x_features = self.dt[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']].values
        # Traning the model
        x_train,x_test,y_train,y_test = train_test_split(x_features,y_target, test_size = 0.3, random_state = 1)
        
        # Train Decision Tree Classifer
        self.tdc = self.tdc.fit(x_train,y_train)

        # Gettign accuracy
        y_pred = self.tdc.predict(x_test)
        print(f'Accuracy:{metrics.accuracy_score(y_test, y_pred)}')   
        return(metrics.accuracy_score(y_test, y_pred))

    def draw_tree(self):
        from io import StringIO 
        from IPython.display import Image, display
        import pydotplus

        out = StringIO()
        tree.export_graphviz(self.tdc, out_file = out)

        graph = pydotplus.graph_from_dot_data(out.getvalue())
        return(graph.write_png('tree.png'))

    def classify_patient(self,patientInfo):
        x_features_recieved = np.array([[patientInfo['age'],patientInfo['sex'],patientInfo['cp'],patientInfo['trestbps'],patientInfo['chol'],patientInfo['fbs'],patientInfo['restecg'],patientInfo['thalach'],patientInfo['oldpeak'],patientInfo['exang'],patientInfo['ca'],patientInfo['slope'],patientInfo['thal']]])
        y_predict_single_pacient = self.tdc.predict(x_features_recieved)
        result = np.int64(y_predict_single_pacient[0]).item()
        return(result)
