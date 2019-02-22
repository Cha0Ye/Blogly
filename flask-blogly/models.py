"""Models for Blogly."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

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
                    default=datetime.now())
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.id'),
                        nullable=False)
    
    user_route = db.relationship('User', backref='post_route')