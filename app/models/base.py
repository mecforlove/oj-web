#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from sqlalchemy import func

from .. import db


class BaseModel(object):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


class TimeMixin(object):
    gmt_created = db.Column(db.DateTime, server_default=func.now())
    gmt_modified = db.Column(db.DateTime, onupdate=func.now())
