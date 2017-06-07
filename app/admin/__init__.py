#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views, errors
