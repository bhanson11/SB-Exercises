from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

RESPONSES = "responses"

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'secret_key!'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route("/")
def show_survey():
    """show survey title, instructions, and button to select survey"""
    return render_template("survey_start.html", survey=survey)

@app.route("/questions/<int:qid>")
def show_question(qid):
    """Display current question"""
    responses = session.get(RESPONSES)

    if (responses is None):
        return redirect("/")
    if (len(responses) == len(survey.questions)):
        #all questions answered
        return redirect("/complete")
    if (len(responses) != qid):
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")
    
    question = survey.questions[qid]
    return render_template("question.html", question_num=qid, question=question)

@app.route("/answer", methods=["POST"])
def handle_question():
    """Save answer and redirect to next question"""

    user_answer = request.form['answer']

    # add this response to the session
    responses = session[RESPONSES]
    responses.append(user_answer)
    session[RESPONSES] = responses

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")
    
@app.route("/complete")
def complete():
    """survey complete. show complete page"""

    return render_template("complete.html")

@app.route("/start", methods=["POST"])
def start_survey():
    """Clear session of responses"""
    session[RESPONSES] = []
    return redirect("/questions/0")
