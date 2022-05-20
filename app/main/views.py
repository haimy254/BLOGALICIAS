

from flask import redirect, render_template,url_for,flash
from flask_login import current_user
from app.main.form import  BlogForm, CommentForm
from app.main import main
from app import db
from ..models import Comment,Blog

@main.route('/')
def index():
    blogs=Blog.query.all
    return render_template('index.html',blogs=blogs)

@main.route('/blog', methods=["GET","POST"])
def add_blog():
    form=BlogForm()
    if form.validate_on_submit():
        blog=Blog(blog=form.blog.data,user_id=current_user.id)
        db.session.add(blog)
        db.session.commit()
        flash ('')
        return redirect(url_for('main.add_blog'))
    return render_template('blog.html', form=form, titile="Add new blog")

@main.route('/comment', methods= ["GET","POST"])
def comment(blog_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data,user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('comment.html', form = form)

@main.route('/blod/<init:blog_id>')
def blog(blog_id):
    blog = Blog.query_or_404(blog_id)
    comments = Comment.query_all()
    form = CommentForm()
    return render_template('blogadd.html', blog=blog, comments=comments, form=form )



