"""Blogly application."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "utahjazz12"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Homepage redirects to user list"""

    return redirect("/users")

@app.route('/users')
def make_users_list():
    """shows all users"""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/list.html', users=users)

@app.route('/users/new', methods=["GET", "POST"])
def new_users():
    """Show form to add new user and handle form submission"""
    if request.method == "POST":
        new_user = User(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            image_url=request.form['image_url'] or None
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(f'/users/{new_user.id}')
    else:
        return render_template('users/new.html')


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("users/details.html", user=user)

@app.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user_info(user_id):
    """edit user details"""
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        user.first_name=request.form['first_name'],
        user.last_name=request.form['last_name'],
        user.image_url=request.form['image_url'] or None
        db.session.commit()
        return redirect(f'/users/{user.id}')
    else:
        return render_template("/users/edit.html", user=user)
    
@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Delete a user completely"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/users")