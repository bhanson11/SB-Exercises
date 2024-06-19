from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY'] = 'Bsecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
        
connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

##################ROUTES
@app.route("/")
def show_pets():
    pets = Pet.query.all()
    return render_template('show_pets.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
