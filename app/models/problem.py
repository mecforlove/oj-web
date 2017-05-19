#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from .. import db
from base import BaseModel, TimeMixin


class Problem(db.Model, BaseModel, TimeMixin):
    __tablename__ = 'problem'

    title = db.Column(db.String(256))
    content = db.Column(db.Text)
    time = db.Column(db.Integer)  # 运行时间限制，单位ms
    mem = db.Column(db.Integer)  # 内存限制，单位KB

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    commits = db.relationship('Commit', backref='problem', lazy='dynamic')


class Course(db.Model, BaseModel, TimeMixin):
    __tablename__ = 'course'

    name = db.Column(db.String(256))  # 课程名
    description = db.Column(db.String(128))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    problems = db.relationship('Problem', backref='course', lazy='dynamic')


class Commit(db.Model, BaseModel, TimeMixin):
    __tablename__ = 'commit'

    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer)  # 状态
    detail = db.Column(db.String(512))  # 详细信息
    language = db.Column(db.String(32))  # 语言
    code = db.Column(db.Text)  # 源代码
    mem = db.Column(db.Integer)  # 内存
    time = db.Column(db.Integer)  # 时间
