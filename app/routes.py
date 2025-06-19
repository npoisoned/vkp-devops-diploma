from flask import current_app as app
from flask import render_template
from .models import User
from . import db

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user/<username>')
def add_user(username):
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return f"User {username} added!"