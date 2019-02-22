"""Models for Blogly."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

def connect_db(app):
        """ connect to db"""                
        db.app = app
        db.init_app(app)

class User(db.Model):
    """User."""
    
    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False,
                    unique=False)
    last_name = db.Column(db.String(50),
                    nullable=False,
                    unique=False)
    image_url = db.Column(db.String(500), 
                    nullable=True, 
                    default='https://www.gettyimages.com/gi-resources/images/CreativeLandingPage/HP_Sept_24_2018/CR3_GettyImages-159018836.jpg')

    # add a new method on User class to call full_name
    def full_name(self):
        return self.first_name + ' ' + self.last_name    

class Post(db.Model):
    """ Post class """

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(200),
                    nullable=False,
                    unique=False)
    content = db.Column(db.Text,
                    nullable=False,
                    unique=False)
    created_at = db.Column(db.DateTime, 
                    default=datetime.now)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.id'),
                        nullable=False)
    
    user_route = db.relationship('User', backref=backref('post_route', cascade= "all, delete-orphan"))


# Added Tag Class
# Added PostTag Class
# to query composite index:
# (((size)::text = 'small'::text) AND ((color)::text = 'red'::text))

    class Tag(db.Model):
    """ Tag class """

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(200),
                    nullable=False,
                    unique=True)


class PostTag(db.Model):
    """ PostTag class """

    __tablename__ = "posttags"

    post_id = db.Column(db.Integer,
                    db.ForeighKey("posts.id")
                    primary_key=True)
    tag_id = db.Column(db.String(200),
                    db.ForeighKey("tags.id")
                    primary_key=True)                    