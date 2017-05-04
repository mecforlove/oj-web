#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from .. import db

from base import BaseModel, TimeMixin


class User(BaseModel, TimeMixin):
    name = db.Column(db.String(128), unique=True)
    passwd = db.Column(db.String(128))
    passwd_hash = db.Column(db.String(32))
    is_teacher = db.Column(db.Boolean)
