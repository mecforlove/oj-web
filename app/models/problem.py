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


class Course(db.Model, BaseModel, TimeMixin):
    __tablename__ = 'course'

    name = db.Column(db.String(256))  # 课程名
