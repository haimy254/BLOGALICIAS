'''all application forms'''
from xmlrpc.client import DateTime
from psycopg2 import Timestamp
from app.models import Comment
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

class BlogForm(FlaskForm):
    blog=StringField('enter the blog')
    
    
class CommentForm(FlaskForm):
    comment = StringField('enter comment')
    submit = SubmitField('blog comments')