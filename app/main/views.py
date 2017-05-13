#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import render_template, request, jsonify, flash, redirect
from flask_login import login_user, login_required, logout_user

from . import main
from ..models.user import User
from ..utils.response import common_response


@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('main/register.html')
    name = request.form.get('username')
    passwd = request.form.get('password')
    new_user = User(name=name, passwd=passwd)
    try:
        new_user.save()
    except Exception as e:
        print e
        return jsonify(common_response(-1, 'register failure'))

    flash(u'注册成功', 'error')
    return jsonify(common_response(0, 'ok'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('main/login.html')
    name = request.form.get('username')
    passwd = request.form.get('password')
    check = User.check_login(name, passwd)
    if check[0]:
        login_user(check[2], True)
        flash(u'登录成功', 'message')
        return redirect('/')
    else:
        flash(check[1], 'error')
        return render_template('main/login.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect('/')
