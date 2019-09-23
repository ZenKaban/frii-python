# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)

from models import *

db.create_all()
db.session.commit()


@app.route('/create', methods=['POST'])
def post():
    from models import Post
    from forms import PostForm

    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)

        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()
            flash('Post created! Post ID ')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

        return 'OK'

@app.route('/comment', methods=['POST'])
def comment_post():
    from models import Comment
    from forms import CommentForm

    if request.method == 'POST':
        print(request.form)
        form = CommentForm(request.form)

        if form.validate():
            print("Validated")
            comment = Comment(**form.data)
            db.session.add(comment)
            db.session.commit()
            flash('Comment posted!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

        return 'OK'
    
@app.route('/', methods = ['GET'])
def read():
    from models import Post, Comment
    
    posts = Post.query.all()
    comments = Comment.query.all()
    
    return render_template('home.txt', posts=posts, comments=comments)


if __name__ == '__main__':
    from models import *
    db.create_all()
    db.session.commit()


    # Running app:
    app.run()
