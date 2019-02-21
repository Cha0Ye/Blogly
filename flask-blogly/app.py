"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def redirect_to_users():
    '''show users'''
    return redirect('/users')


@app.route('/users')
def show_users():
    '''Get / render the list of users'''
    users = User.query.all()

    return render_template('users.html', users = users)


@app.route('/users/new')
def new_user():
    '''create new user'''

    return render_template('newuser.html')


@app.route('/users', methods = ['POST'])
def create_new_user():
    '''show users'''
    new_first_name = request.form.get('first-name')
    new_last_name  = request.form.get('last-name')
    new_image_url = request.form.get('image-url')

    new_user = User(first_name = new_first_name, last_name = new_last_name, image_url=new_image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')    


# @app.route('/users/new', methods = ['POST'])
# def new_user():
#     '''create new user'''

#     return render_template('newuser.html')





# db.create_all()
