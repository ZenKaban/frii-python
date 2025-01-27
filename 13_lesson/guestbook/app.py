# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/create', methods=['POST'])
def post():
    from models import Post, User
    from forms import PostForm

    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)

        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

@app.route('/', methods = ['GET'])
def read():
    from models import Post, User
    from forms import PostForm
    
    posts = Post.query.all()
    #user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user
    
    for post in posts:
        # user_id = post.user_id
        # user = User.query.filter_by(id=user_id).first()
        user = post.user
        print(post.user_id, user)
        user = post.user
        print(post.user)
    
    return render_template('home.txt', posts=posts)


def populate_db():
    print('Creating default user')
    # Creating new ones:
    ivan = User(username='Ivan', email='p@p.com')

    db.session.add(ivan)
    db.session.commit()  # note


if __name__ == '__main__':
    from models import *
    db.create_all()
    Post.query.delete()
    db.session.commit()

    if User.query.count() == 0:
        populate_db()

    users = User.query.all()
    print(list(map(str, users)))

    # Running app:
    app.run()
