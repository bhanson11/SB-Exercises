from flask import Flask, jsonify, render_template, request, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "BOGGLEROCKS"

app.config['TESTING'] = True

boggle_game = Boggle()

@app.route("/")
def home():
    """Show boggle game board"""
    board = boggle_game.make_board()
    session['board'] = board
    session['score'] = 0
    session['guessed_words'] = []

    return render_template("index.html", board=board, score=session['score'])

@app.route("/submit-word", methods=["POST"])
def submit_word():
    """Submit word to check if it is a valid word and if it is on the game board"""
    
    word = request.json.get("word")  # Use get to avoid KeyError
    board = session.get("board", [])
    
    response = boggle_game.check_valid_word(board, word)

    session.setdefault('guessed_words', [])  # Change set() to []

    # Include the guessed words only if the word is valid and not already guessed
    if response == 'ok' and word not in session['guessed_words']:
        session['guessed_words'].append(word)  # Change add() to append()
        session.modified = True

    print('Session:', session)
    print('Guessed Words:', session['guessed_words'])  # added for debugging

    # Always include the guessed_words field in the response as an array
    return jsonify(result=response, score=session['score'], guessed_words=session['guessed_words'])


@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update num_plays, update high score if appropriate."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    num_plays = session.get("num_plays", 0)

    session['num_plays'] = num_plays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)