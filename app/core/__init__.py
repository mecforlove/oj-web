#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from compile import compile_src
from judge import judge, judge_one_mem_time, judge_result


def task(problem_id, commit_id, lan):
    compile_src(commit_id, lan)
