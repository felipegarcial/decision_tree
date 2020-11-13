from flask import Flask,jsonify,request
from model.tree import DesitionTree

d_tree= DesitionTree()

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return jsonify({'message':'Hello world!'})
@app.route('/desitionTree')
def getDecisionTree():
    return jsonify({'message':'Image desition tree'})
@app.route('/classifier',methods=['POST'])
def classifiedPacient():
    return jsonify({'message':d_tree.classify_patient(request.json)})

if __name__ == '__main__':
    app.run(debug=True,port=4000,host='0.0.0.0')
