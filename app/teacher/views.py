#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import render_template, request, jsonify, flash
from flask_login import current_user, login_required

from . import teachers
from ..models.problem import Course, Problem
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
    flash(u'保存成功')
    return jsonify(common_response(0, 'ok'))


@teachers.route('/del_course', methods=['POST'])
@login_required
def del_course():
    course_id = int(request.form.get('id', 0))
    course = Course.query.get(course_id)
    course.delete()
    flash(u'删除成功')
    return jsonify(common_response(0, 'ok'))


@teachers.route('/problems')
@login_required
def show_problems():
    course_id = request.args.get('course_id', 0)
    if course_id:
        course_id = int(course_id)
    course = Course.query.get(course_id)
    problems = course.problems
    return render_template('/teacher/problems.html', problems=problems,
                           course=course)


@teachers.route('/save_problem', methods=['POST'])
@login_required
def save_problem():
    course_id = request.form.get('course_id')
    problem_id = request.form.get('id', 0)
    title = request.form.get('title')
    content = request.form.get('content')
    time = request.form.get('time')
    mem = request.form.get('mem')
    if problem_id:
        problem_id = int(problem_id)
        problem = Problem.query.get(problem_id)
        problem.title = title
        problem.content = content
        problem.time = time
        problem.mem = mem
    else:
        problem = Problem(title=title, content=content, time=time, mem=mem,
                          course_id=course_id)
    problem.save()
    flash(u'题目保存成功')
    return jsonify(common_response(0, 'ok'))


@teachers.route('/del_problem', methods=['POST'])
@login_required
def del_problem():
    problem_id = int(request.form.get('id', 0))
    problem = Problem.query.get(problem_id)
    problem.delete()
    flash(u'题目删除成功')
    return jsonify(common_response(0, 'ok'))
