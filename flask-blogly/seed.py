"""Seed file to make sample data for pets db."""

from models import User, db, Post
from app import app

# Create all tables
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
alan = User(first_name='Alan', last_name='Alda')
joel = User(first_name='Joel', last_name='Burton')
jane = User(first_name='Jane', last_name='Smith')
sara = User(first_name='Sara', last_name='Zare', image_url='flask-blogly/Sara.jpg')
chao = User(first_name='Chao', last_name='Ye', image_url='flask-blogly/Chao.jpg')

# Add new objects to session, so they'll persist
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)
db.session.add(sara)
db.session.add(chao)

db.session.commit()

#create posts for various users
alanpost = Post(title='Alan Post1', content='Alan adsfdsfdsfdsfdsfdsfdfdsfds', created_at="2017-01-03" , user_id= alan.id)
joelpost = Post(title='Joel Post1', content='Joel randomaldkfadsl', created_at="2017-01-04" , user_id =joel.id)
joelpost2 = Post(title='Joel Post2', content='Joel2 lkajsdfljksd', created_at="2017-01-05" , user_id =joel.id)
sarapost = Post(title='Sara Post1', content='Sara adfsd', created_at="2017-01-06" , user_id =sara.id)
chaopost = Post(title='Chao Post1', content='Chao lasdkjflaisd', created_at="2017-01-07", user_id =chao.id)

# Add new objects to session, so they'll persist
db.session.add(alanpost)
db.session.add(joelpost)
db.session.add(joelpost2)
db.session.add(sarapost)
db.session.add(chaopost)


# Commit--otherwise, this never gets saved!
db.session.commit()