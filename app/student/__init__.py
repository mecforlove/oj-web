#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import Blueprint

students = Blueprint('students', __name__)

from views import show_problems