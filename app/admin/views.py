#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import render_template, redirect, flash

from . import admin
from ..models.user import User
from ..models.problem import Problem


@admin.route('/users')
def show_users():
    users = User.query.all()
    return render_template('/admin/users.html', users=users)


@admin.route('/users/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    user.delete()
    flash(u'用户删除成功')
    return redirect('/admin/users')


@admin.route('/problems')
def show_problems():
    problems = Problem.query.all()
    return render_template('/admin/problems.html', problems=problems)


@admin.route('/problems/<int:problem_id>')
def delete_problem(problem_id):
    problem = Problem.query.get(problem_id)
    problem.delete()
    flash(u'题目删除成功')
    return redirect('/admin/problems')
