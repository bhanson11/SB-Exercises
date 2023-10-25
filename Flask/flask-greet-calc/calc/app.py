# Put your app in here.
from flask import Flask
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def solve_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = add(a,b)
    return result


@app.route('/sub')
def solve_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = sub(a,b)
    return result

@app.route('/mult')
def solve_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = mult(a,b)
    return result

@app.route('/div')
def solve_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = div(a,b)
    return result