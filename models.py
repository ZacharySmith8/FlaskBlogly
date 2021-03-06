"""Models for Blogly."""
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from sqlalchemy.orm import backref

from sqlalchemy.sql.elements import False_
from sqlalchemy.sql.schema import PrimaryKeyConstraint

db = SQLAlchemy()
def connect_db(app):
    '''Connects Database'''
    db.app=app
    db.init_app(app)


class User(db.Model):
    '''Creates Users Table'''
    __tablename__='users'
    id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    fname= db.Column(db.String(20),nullable=False)
    lname= db.Column(db.String(25),nullable=False)
    image= db.Column(db.String,nullable=False,default='https://thumbs.dreamstime.com/b/default-avatar-profile-icon-social-media-user-vector-default-avatar-profile-icon-social-media-user-vector-portrait-176194876.jpg'
)
    posts = db.relationship('Post',backref="user")
    def __repr__(self):
        return f"<{self.get_full_name()}>"
    
    def get_full_name(self):
       name = "{fname} {lname}".format(fname=self.fname,lname=self.lname)

       return name;


class Post(db.Model):
    '''Creates Post Table'''
    
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(25),nullable=False)
    content=db.Column(db.String(500),nullable=False)
    created_at=db.Column(db.String,default = datetime.now())
    user_id= db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f"<{self.title},{self.content},{self.user_id}>"

class Tag(db.Model):
    '''Creates Tag Table'''

    __tablename__ = "tags"
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10), nullable=False,unique=True)
    posts = db.relationship("Post", secondary = "PostTags", backref="tags")
    def __repr__(self):
        return f"<{self.name}>"

class PostTag(db.Model):
    __tablename__= "PostTags"
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"),primary_key=True)
    tag_id = db.Column(db.Integer,db.ForeignKey("tags.id"),primary_key=True)
    

