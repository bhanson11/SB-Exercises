"""Blogly application."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

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

###########################USERS ROUTES

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

###########################POSTS ROUTES

@app.route("/users/<int:user_id>/posts/new/", methods=["GET", "POST"])
def new_post(user_id):
    """handle form submission for creating a new post for a user"""
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        new_post = Post(
            title=request.form['title'],
            content=request.form['content'],
            user_id=user_id
            )
    
        db.session.add(new_post)
        db.session.commit()

        return redirect(f"/users/{user_id}")
    
    else:
        return render_template('/posts/new.html', user=user)
    
@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """Show a page for a specific post and its details"""

    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    return render_template('posts/details.html', post=post, user=user)

@app.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    """Show form to edit post"""

    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)

    if request.method == "POST":
        post.title=request.form['title'],
        post.content=request.form['content'],
        
        db.session.commit()
        return redirect(f"/posts/{post.id}")
    else: 
        return render_template('posts/edit.html', post=post, user=user)

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def eliminate_post(post_id):
    """delete post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    return redirect(f"/users/{post.user_id}")