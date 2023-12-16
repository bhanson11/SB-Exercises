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

@app.route("/submit-word")
def submit_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify([{'result': response}])

@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update num_plays, update high score if appropriate."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    num_plays = session.get("num_plays", 0)

    session['num_plays'] = num_plays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)