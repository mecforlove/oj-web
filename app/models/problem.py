#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from .. import db
from base import BaseModel, TimeMixin


class Problem(db.Model, BaseModel, TimeMixin):
    pass
