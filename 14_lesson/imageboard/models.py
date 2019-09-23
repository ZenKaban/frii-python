# -*- coding: utf-8 -*-

from datetime import date

from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    # is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return '<Post %r>'.format(self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id'),
        nullable=False,
        index=True
    )
    # post_transform = db.relationship(Post, foreign_keys=[post_id, ])

    # title = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)

    date_created = db.Column(db.Date, default=date.today)
    # is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return '<Post %r,>'.format(self.title, self.user_id)
