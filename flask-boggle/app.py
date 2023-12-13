from flask import Flask, render_template, request, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "BOGGLEROCKS"

boggle_game = Boggle()

@app.route("/")
def home():
    """Show boggle game board"""
    board = boggle_game.make_board()
    # session['board'] = board
    # highscore = session.get("highscore", 0)
    # num_plays = session.get("num_plays", 0)

    return render_template("index.html", board=board)

@app.route("/verify-word")
def verify_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    