'''all application forms'''

from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class CommentForm(FlaskForm):
    comment = StringField('enter comment')
    submit = SubmitField('blog comments')
    
    
class BlogForm(FlaskForm):
    blog =  StringField('')
    submit = SubmitField('submit')


    
