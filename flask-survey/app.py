from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

RESPONSES = []

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'secret_key!'
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route("/")
def show_survey():
    """show survey title, instructions, and button to select survey"""
    return render_template("survey_start.html", survey=survey)

@app.route("/start", methods=["POST"])
def start_survey():
    """Clear session of responses"""
    session[RESPONSES] = []
    return redirect("/questions/0")

