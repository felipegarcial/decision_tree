class DesitionTree:
    def __init__(self):
        print("Entro")

    def classify_patient(self,patientInfo):
        return (f"Los datos de entrada:{patientInfo['age']},{patientInfo['sex']},{patientInfo['cp']},{patientInfo['trestbps']},{patientInfo['chol']},{patientInfo['fbs']},{patientInfo['restecg']},{patientInfo['thalach']},{patientInfo['exang']},{patientInfo['oldpeak']},{patientInfo['slope']},{patientInfo['ca']},{patientInfo['thal']}") 

