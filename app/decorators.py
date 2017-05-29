#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import abort

from functools import wraps
from flask_login import current_user


# 管理员中间件
def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_admin:
            return func(*args, **kwargs)
        abort(403)  # 鉴权失败

    return wrapper


# 教师中间件
def teacher_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_teacher:
            return func(*args, **kwargs)
        abort(403)

    return wrapper
