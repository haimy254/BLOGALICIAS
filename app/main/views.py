

from flask import redirect, render_template,url_for
from flask_login import current_user
from app.main.form import  BlogForm, CommentForm
from app.main import main
from app import db
from ..models import Comment,Blog

@main.route('/')
def index():
    blogs=Blog.query.all()
    comments = Comment.query_all()
    form = CommentForm()
    return render_template('index.html',blogs=blogs,comments=comments,form=form)

@main.route('/blog', methods=["GET","POST"])
def blog():
    form=BlogForm()
    if form.validate_on_submit():
        blog=Blog(blog=form.blog.data,user_id=current_user.id)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.blog'))
    return render_template('index.html', form=form)

@main.route('/comment', methods= ["GET","POST"])
def comment(blog_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data, blog_id=current_user, blog_id=blog_id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index', blog_id=blog_id))
    return render_template('comment.html', form = form)




