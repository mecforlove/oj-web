#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import render_template, request, jsonify
from flask_login import current_user, login_required

from . import teachers
from ..models.problem import Course
from ..utils.response import common_response


@teachers.route('/courses')
@login_required
def show_courses():
    courses = Course.query.filter_by(user_id=current_user.id).all()
    return render_template('/teacher/courses.html', courses=courses)


@teachers.route('/save_course', methods=['POST'])
@login_required
def save_course():
    course_id = request.form.get('id', 0)
    name = request.form.get('name')
    description = request.form.get('description')
    if course_id:
        course_id = int(course_id)
        course = Course.query.get(course_id)
        course.name = name
        course.description = description
    else:
        course = Course(name=name, description=description,
                        user_id=current_user.id)
    course.save()
    return jsonify(common_response(0, 'ok'))


@teachers.route('/del_course', methods=['POST'])
@login_required
def del_course():
    course_id = int(request.form.get('id', 0))
    course = Course.query.get(course_id)
    course.delete()
    return jsonify(common_response(0, 'ok'))
