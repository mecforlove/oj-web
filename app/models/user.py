#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask_login import UserMixin

from .. import db, login_manager
from base import BaseModel, TimeMixin


class User(db.Model, BaseModel, TimeMixin, UserMixin):
    __tablename__ = 'user'

    name = db.Column(db.String(128), unique=True)
    passwd = db.Column(db.String(128))
    passwd_hash = db.Column(db.String(32))
    is_teacher = db.Column(db.Boolean, default=False)

    admins = db.relationship('Admin', backref='user', lazy='dynamic')

    @classmethod
    def check_login(cls, name, passwd):
        user = User.query.filter_by(name=name).first()
        if user is None:
            return False, 'user not exists'
        if user.passwd != passwd:
            return False, 'wrong password'
        return True, 'login success', user

    @property
    def is_admin(self):
        return self.id in [i.user_id for i in self.admins]


class Admin(db.Model, BaseModel, TimeMixin):
    __tablename__ = 'admin'

    description = db.Column(db.String(128))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
