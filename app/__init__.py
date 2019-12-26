from flask import Flask,request,jsonify

from app.Customer import Customer

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello World"


@app.route('/greet/<name>',methods =['POST'])
def greet(name):
    return "how are you doing " + name

@app.route('/createcustomer',methods=['POST'])
def createcustomer():
    content=request.get_json()
    print(content)
    return content

@app.route('/getcustomer/<firstname>',methods=['GET'])
def getcustomer(firstname):
    newcustomer=Customer(firstname,firstname,25)
    return jsonify(newcustomer.__dict__)
