from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<Madlibs>'

toolbar = DebugToolbarExtension(app)

@app.route("/")
def fill_prompts():
    """Generate and show form to ask words."""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)