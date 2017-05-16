#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import Blueprint

teachers = Blueprint('teachers', __name__)

from views import show_courses