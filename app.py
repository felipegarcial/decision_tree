from flask import Flask,jsonify,request
from model.tree import DecisionTree

d_tree= DecisionTree()

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return jsonify({'message':'Hello world!'})

@app.route('/train')
def train_model():
    return jsonify({
        'message':'Arbol dibujado',
        'url': d_tree.train_model()
    })

@app.route('/draw-tree')
def draw_tree():
    return jsonify({
        'message':'Modelo entrenado',
        'Accuracy': d_tree.draw_tree()
    })


@app.route('/classify-patient',methods=['POST'])
def classified_patient():
    return jsonify({
        'message':'Paciente clasificado',
        'classified':d_tree.classify_patient(request.json)
        
    })

if __name__ == '__main__':
    app.run()
