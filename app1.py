from flask import Flask, jsonify , request

app = Flask(__name__)


items = [
    {
        'number': '2'
    }
]
number= 2
@app.route('/')
def hello():
    return "<h1>HELLO, MATHEMATICS<h1>"


@app.route('/add/2/2')
def add(number):
    a = number+number
    return str(a)

@app.route('/multiply/2/2')
def multiply(number):
    a = number*number
    return str(a)


@app.route('/divide/<int:number>')
def divide(number):
    a = number/number
    return str(a)


@app.route('/sub/<int:number>')
def sub(number):
    a = number-number
    return str(a)

app.run()