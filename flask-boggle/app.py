from flask import Flask
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "BOGGLEROCKS"

boggle_game = Boggle()

@app.route("/")
def home():
    """Show boggle game board"""
    return "Welcome to....BOGGLE!!"