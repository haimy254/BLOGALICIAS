

from flask import redirect, render_template,url_for,abort
from flask_login import current_user
from app.main.form import  BlogForm, CommentForm
from app.main import main
from app import db
from ..models import Comment,Blog

@main.route('/')
def index():
    blogs=Blog.query.all()
    comments = Comment.query.all()
    form = CommentForm()
    return render_template('index.html',blogs=blogs,comments=comments,form=form)

@main.route('/blog', methods=["GET","POST"])
def blog():
    form=BlogForm()
    if form.validate_on_submit():
        blog=Blog(blog=form.blog.data,user_id=current_user.id,comment=comment)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('blog.html', form=form)

@main.route('/comment', methods= ["GET","POST"])
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data, user_id=current_user)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('comment.html', form = form)

@main.route('/blog', methods= ["POST"])
def delete_blog():
    blog = Blog.query.get_or_404()
    if blog.user_id !=current_user:
        abort(403)
    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('main.index'))






