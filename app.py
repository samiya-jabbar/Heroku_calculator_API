from flask import Flask, jsonify , request
  
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("test.html")

@app.route('/add/<int:usernumber1>/<int:usernumber2>')
def add(usernumber1, usernumber2):
    a= usernumber1+usernumber2
    return "The sum of these two numbers is %s" % a

@app.route('/multiply/<int:usernumber1>/<int:usernumber2>')
def multiply(usernumber1, usernumber2):
    a= usernumber1*usernumber2
    return "The product of these two numbers is %s" % a

@app.route('/divide/<int:usernumber1>/<int:usernumber2>')
def divide(usernumber1, usernumber2):
    a= usernumber1/usernumber2
    return "The result of these two numbers is %s" % a

@app.route('/sub/<int:usernumber1>/<int:usernumber2>')
def sub(usernumber1, usernumber2):
    a= usernumber1-usernumber2
    return "The difference of these two numbers is %s" % a

if __name__=="__main__":
    app.run()
