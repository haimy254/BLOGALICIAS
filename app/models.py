from app import db
from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username= db.Column(db.String(300),unique = True,index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_s =db.Column(db.String(300))
    profile_pic_path = db.Column(db.String(255))
    bio = db.Column(db.String(600))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    blogs = db.relationship('Blog', backref='users', lazy='dynamic')
    comments = db.relationship('Comment', backref='users', lazy='dynamic')
    upvote = db.relationship('Upvote', backref = 'users', lazy = 'dynamic')
    downvote = db.relationship('Downvote', backref = 'users', lazy = 'dynamic')
  
 
    @property
    def password(self):
      raise AttributeError('this is restriced')
  
    @password.setter
    def password(self,password):
        self.pass_s = generate_password_hash(password)
        
    def verify_hash(self,password):
        return check_password_hash(self.pass_s, password)
    
    def __repr__(self):
        return f'User{self.username}'
    
class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer,primary_key = True)
    blog = db.Column(db.String(300),index = True)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.Integer,db.ForeignKey("users.id"), nullable = False)
    comments = db.relationship('Comment',backref='blogs',lazy='dynamic') 
    upvotes = db.relationship('Upvote', backref = 'blogs', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'blogs', lazy = 'dynamic')
    
    def __repr__(self):
       return f'Pitch{self.description}'
   
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    username = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return f'<Comment: {self.comment}>'


class Upvote(db.Model):
    __tablename__ = 'upvotes'
    
    id = db.Column(db.Integer,primary_key = True)
    upvote = db.Column(db.Integer,default=1)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def __repr__(self):
       return f'Upvote{self.upvotes}'
   
class Downvote(db.Model):
    __tablename__ = 'downvotes'
    
    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(db.Integer,default=1)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def __repr__(self):
       return f'Downvote{self.downvotes}'
    
  
