# Put your app in here.
from flask import Flask

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = a + b
    return result


@app.route('/sub')
def subtract():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = a - b
    return result

@app.route('/mult')
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = a * b
    return result

@app.route('/div')
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = a / b
    return result