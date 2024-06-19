from flask import Flask, render_template, redirect, url_for
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
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=True)
        db.session.add(new_pet)
        db.session.commit()
        
        return redirect(url_for('show_pets'))
    return render_template('add_pet.html', form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        return redirect(url_for('show_pets'))
    return render_template('pet_detail.html', pet=pet, form=form)