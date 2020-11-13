from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/')
def helloWorld():
    return jsonify({'message':'Hello world!'})
@app.route('/desitionTree')
def getDecisionTree():
    return jsonify({'message':'Image desition tree'})
@app.route('/desitionTree')


if __name__ == '__main__':
    app.run(debug=True,port=4000,host='0.0.0.0')
