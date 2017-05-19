#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import render_template
from flask_login import login_required

from . import students
from ..models.problem import Problem


@students.route('/problems')
@login_required
def show_problems():
    problems = Problem.query.all()
    return render_template('/student/problems.html', problems=problems)
