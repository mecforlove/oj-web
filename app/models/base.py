#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from sqlalchemy import func

from .. import db


class BaseModel(object):
    # 自增主键id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 保存实体
    def save(self):
        db.session.add(self)
        db.session.commit()

    # 删除实体
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class TimeMixin(object):
    """
    时间混入model
    """
    gmt_created = db.Column(db.DateTime, server_default=func.now())
    gmt_modified = db.Column(db.DateTime, onupdate=func.now())
