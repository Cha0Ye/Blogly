"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import func # day of the week
from datetime import datetime

# from flask_sqlalchemy import SQLAlchemy


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
    return redirect('/404.html')

############ SHOW USERS PAGE ############

@app.route('/users')
def show_users():
    '''Get / render the list of users'''
    users = User.query.all()
    
    return render_template('users.html', users = users)

############ ADD NEW USERS ############

@app.route('/users/new')
def new_user():
    '''show: /newuser.html
    create new user'''

    return render_template('newuser.html')

@app.route('/users', methods = ['POST'])
def create_new_user():
    ''' show: /users
    create new users and redirect to users page'''
    new_first_name = request.form.get('first-name') 
    new_last_name  = request.form.get('last-name') 
    new_image_url = request.form.get('image-url') 

    # new_first_name = request.form.get('first-name') or None
    # new_last_name  = request.form.get('last-name') or None
    # new_image_url = request.form.get('image-url') or None

    # if new_first_name == "":
    #     raise ValueError('all fielsds must be submitted')

    new_user = User(first_name = new_first_name, last_name = new_last_name, image_url=new_image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

############ SHOW EXISTING USER PAGE ############

@app.route('/users/<int:userid>')
def show_user_info(userid):
    '''show: /userpage.html
    users info'''
    user = User.query.get(userid)
    posts=user.post_route

    return render_template('userpage.html', user = user, posts=posts)


############ EDIT EXISTING USERS PAGE ############

@app.route('/users/<int:userid>/edit')
def render_edit_user(userid):
    ''' show: /edituser.html
    Edit existing user'''
    user = User.query.get(userid)

    return render_template('edituser.html', user = user)

@app.route('/users/<int:userid>/edit', methods = ['POST'])
def save_edit_user_info(userid):
    '''create new users and redirect to users page'''
    user = User.query.get(userid)
    user.first_name  = request.form.get('first-name')
    user.last_name  = request.form.get('last-name')
    user.image_url = request.form.get('image-url')
    
    db.session.commit()

    return redirect('/users')

############ DELETE USER  ############

@app.route('/users/<int:userid>/delete', methods=['POST'])
def delete_user_info(userid):
    '''delete user info'''
    user = User.query.get(userid)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')    


########### ADD POSTS IN USER PAGE ############
@app.route('/users/<int:userid>/posts/new')
def render_add_new_post(userid):
    '''render Add New post form '''
    user = User.query.get(userid)

    return render_template('newpost.html', user=user)


@app.route('/users/<int:userid>/posts', methods=['POST'])
def handle_new_post(userid):
    '''Handle new post'''
    user = User.query.get(userid)

    post_title  = request.form.get('post-title')
    post_content  = request.form.get('post-content')
    post_user_id = userid
    
    new_post = Post(title = post_title, content = post_content, user_id = post_user_id)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{userid}')

########### RENDER SHOW POST ############
@app.route('/posts/<int:postid>')
def show_post(postid):
    '''Show Post '''
    
    post = Post.query.get(postid)
    user = post.user_route

    return render_template('showpost.html', post=post, user=user)


########### SHOW EDIT POST ############
@app.route('/posts/<int:postid>/edit')
def render_edit_post(postid):
    ''' Render post edit page'''

    post = Post.query.get(postid)
    user = post.user_route
    return render_template('editpost.html', user= user, post = post)

########### SAVE EDIT POST ############
@app.route('/posts/<int:postid>/edit', methods=['POST'])
def save_edit_post(postid):
    '''Handle edited post data'''
    post = Post.query.get(postid)

    post.title  = request.form.get('post-title')
    post.content  = request.form.get('post-content')

    db.session.commit()

    return redirect(f'/posts/{postid}')

############ DELETE POST  ############

@app.route('/posts/<int:postid>/delete', methods=['POST'])
def delete_post(postid):
    '''delete post and redirect to users page'''
    post = Post.query.get(postid)
    
    # user = post.user_route
    userid = post.user_route.id

    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{userid}')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

    # post.query.order_by('created_at desc').limit(5)
    # .filter(extract('year', Foo.Date) 
    # .filter(extract('month', Foo.Date)

# Add day of week:
# dow = func.extract(<my_object>, 'dow')