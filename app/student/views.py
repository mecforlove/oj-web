#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
import os

from flask import render_template, request, jsonify
from flask_login import login_required, current_user

from . import students
from ..models.problem import Problem, Commit, Course
from ..utils.response import common_response
from ..core.compile import compile_src
from ..core import judge


@students.route('/problems')
@login_required
def show_problems():
    problems = Problem.query.all()
    for p in problems:
        try_times = Commit.query.filter_by(problem_id=p.id).count()
        pass_times = Commit.query.filter_by(problem_id=p.id,
                                            status=1).count()
        if try_times:
            pass_rate = pass_times / try_times
        else:
            pass_rate = 0.0
        setattr(p, 'try_times', try_times)
        setattr(p, 'pass_times', pass_times)
        setattr(p, 'pass_rate', pass_rate)
    return render_template('/student/problems.html', problems=problems)


@students.route('/courses')
@login_required
def show_courses():
    courses = Course.query.all()
    print len(courses)
    return render_template('/student/courses.html', courses=courses)


@students.route('/problems/<int:p_id>')
def show_problem(p_id):
    problem = Problem.query.get(p_id)
    content = problem.content  # 纯文本
    # 将纯文本渲染下以便前端显示
    problem.content = content.replace('\n', '<br/ >')
    return render_template('/student/problem_detail.html', problem=problem)


@students.route('/commit', methods=['POST'])
def commit():
    lan = request.form.get('lan')  # 语言种类
    src = request.form.get('src')  # 源代码
    problem_id = int(request.form.get('problem_id'))  # 问题id
    new_commit = Commit(problem_id=problem_id, language=lan, code=src,
                        status=0, user_id=current_user.id,
                        detail=u'Accept', mem=10220, time=503)
    new_commit.save()
    work_dir = '/Users/mec/oj_work/%s' % new_commit.id
    os.mkdir(work_dir)  # 创建工作目录
    if lan.lower() == 'c':
        with open(work_dir + '/main.c', 'w') as f:
            f.write(src)
    elif lan.lower() == 'python':
        with open(work_dir + 'main.py', 'w') as f:
            f.write(src)
    else:
        return jsonify(common_response(-1, 'language not support'))
    compile_src(new_commit.id, lan)
    judge(problem_id, new_commit.id)
    return jsonify(common_response(0, 'ok'))


@students.route('/commits')
def show_commits():
    commits = Commit.query.all()
    return render_template('/main/commits.html', commits=commits)

