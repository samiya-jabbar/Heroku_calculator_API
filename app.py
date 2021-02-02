from flask import Flask, jsonify , request

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>HELLO, MATHEMATICS<h1>"

@app.route('/add/2/2')
def add():
    a = 2+2
    return str(a)

@app.route('/multiply/2/2')
def multiply():
    a= 2*2
    return str(a)

@app.route('/divide/2/2')
def divide():
    a= 2/2
    a=int(a)
    return str(a)

@app.route('/sub/2/2')
def sub():
    a= 2-2
    return str(a)

if __name__=="__main__":
    app.run()
