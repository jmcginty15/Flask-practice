# Put your app in here.
from flask import Flask
from flask import request
from operations import *

app = Flask(__name__)

@app.route('/<op>')
def operate(op):
    operations = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations[op](a, b))

@app.route('/math/<op>')
def operator_the_second(op):
    operations = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations[op](a, b))