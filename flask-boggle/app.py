from flask import Flask, jsonify, render_template, request, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "BOGGLEROCKS"

boggle_game = Boggle()

@app.route("/")
def home():
    """Show boggle game board"""
    board = boggle_game.make_board()
    session['board'] = board

    return render_template("index.html", board=board)

@app.route("/check-word-validity")
def check_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify([{'result': response}])

    