#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
import os
import subprocess
import time

from compile import compile_src
from ..models.problem import Commit
from .. import db
from config import *


def judge_one(in_file, out_file, commit):
    ifile = open(in_file)
    lan = commit.language
    if lan.lower() == 'c':
        cmd = './main'
    elif lan.lower() == 'python':
        cmd = 'python main.py'
    elif lan.lower() == 'c++':
        cmd = './main'
    start_time = time.time()
    p = subprocess.Popen(
        cmd,
        shell=True,
        cwd=work_dir + '/%s' % commit.id,
        stdin=ifile,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out, error = p.communicate()
    end_time = time.time()
    t = end_time - start_time
    with open(out_file) as f:
        o = f.read()
        if out == o:
            return True, t
    return False, 'error'


def judge(problem_id, commit_id):
    commit = Commit.query.get(commit_id)
    cnt = len(os.listdir(data_dir + '/%s' % problem_id))
    time_sum = 0
    for i in range(cnt / 2):
        in_file = data_dir + '/%s/' % problem_id + '%s.in' % i
        out_file = data_dir + '/%s/' % problem_id + '%s.out' % i
        ret = judge_one(in_file, out_file, commit)
        if not ret[0]:
            commit.status = 3
            commit.detail = 'Wrong Answer'
            break
        time_sum += ret[1]
    commit.status = 2
    commit.time = time_sum / cnt

    db.session.commit()
