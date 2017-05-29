#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
import os
import logging
import shlex
import lorun

from .. import db

data_dir = '/home/www/data'
work_dir = '/home/www/work'


def judge_one_mem_time(
        commit_id, problem_id, data_num, time_limit, mem_limit, language):
    """评测一组数据"""
    input_path = os.path.join(
        data_dir, str(problem_id), 'data%s.in' %
        data_num)
    try:
        input_data = file(input_path)
    except:
        return False
    output_path = os.path.join(
        work_dir, str(commit_id), 'out%s.txt' %
        data_num)
    temp_out_data = file(output_path, 'w')
    if language == 'java':
        cmd = 'java -cp %s Main' % (
            os.path.join(work_dir,
                         str(commit_id)))
        main_exe = shlex.split(cmd)
    elif language == 'python2':
        cmd = 'python2 %s' % (
            os.path.join(work_dir, str(commit_id), 'main.pyc'))
        main_exe = shlex.split(cmd)
    elif language == 'python3':
        cmd = 'python3 %s' % (
            os.path.join(work_dir,
                         str(commit_id),
                         '__pycache__/main.cpython-33.pyc'))
        main_exe = shlex.split(cmd)
    elif language == 'lua':
        cmd = "lua %s" % (
            os.path.join(work_dir,
                         str(commit_id),
                         "main"))
        main_exe = shlex.split(cmd)
    elif language == "ruby":
        cmd = "ruby %s" % (
            os.path.join(work_dir,
                         str(commit_id),
                         "main.rb"))
        main_exe = shlex.split(cmd)
    elif language == "perl":
        cmd = "perl %s" % (
            os.path.join(work_dir,
                         str(commit_id),
                         "main.pl"))
        main_exe = shlex.split(cmd)
    else:
        main_exe = [os.path.join(work_dir, str(commit_id), 'main'), ]
    runcfg = {
        'args': main_exe,
        'fd_in': input_data.fileno(),
        'fd_out': temp_out_data.fileno(),
        'timelimit': time_limit,  # in MS
        'memorylimit': mem_limit,  # in KB
    }
    rst = lorun.run(runcfg)
    input_data.close()
    temp_out_data.close()
    logging.debug(rst)
    return rst


def judge_result(problem_id, commit_id, data_num):
    """对输出数据进行评测"""
    logging.debug("Judging result")
    correct_result = os.path.join(
        data_dir, str(problem_id), 'data%s.out' %
        data_num)
    user_result = os.path.join(
        work_dir, str(commit_id), 'out%s.txt' %
        data_num)
    try:
        correct = file(
            correct_result).read(
            ).replace(
                '\r',
                '').rstrip(
                )  # 删除\r,删除行末的空格和换行
        user = file(user_result).read().replace('\r', '').rstrip()
    except:
        return False
    if correct == user:  # 完全相同:AC
        return "Accepted"
    if correct.split() == user.split():  # 除去空格,tab,换行相同:PE
        return "Presentation Error"
    if correct in user:  # 输出多了
        return "Output limit"
    return "Wrong Answer"  # 其他WA


def judge(commit_id, problem_id, data_count, time_limit,
          mem_limit, program_info, result_code, language):
    """评测编译类型语言"""
    max_mem = 0
    max_time = 0
    if language in ["java", 'python2', 'python3', 'ruby', 'perl']:
        time_limit = time_limit * 2
        mem_limit = mem_limit * 2
    for i in range(data_count):
        ret = judge_one_mem_time(
            commit_id,
            problem_id,
            i + 1,
            time_limit + 10,
            mem_limit,
            language)
        if ret == False:
            continue
        if ret['result'] == 5:
            program_info['result'] = result_code["Runtime Error"]
            return program_info
        elif ret['result'] == 2:
            program_info['result'] = result_code["Time Limit Exceeded"]
            program_info['take_time'] = time_limit + 10
            return program_info
        elif ret['result'] == 3:
            program_info['result'] = result_code["Memory Limit Exceeded"]
            program_info['take_memory'] = mem_limit
            return program_info
        if max_time < ret["timeused"]:
            max_time = ret['timeused']
        if max_mem < ret['memoryused']:
            max_mem = ret['memoryused']
        result = judge_result(problem_id, commit_id, i + 1)
        if result == False:
            continue
        if result == "Wrong Answer" or result == "Output limit":
            program_info['result'] = result_code[result]
            break
        elif result == 'Presentation Error':
            program_info['result'] = result_code[result]
        elif result == 'Accepted':
            if program_info['result'] != 'Presentation Error':
                program_info['result'] = result_code[result]
        else:
            logging.error("judge did not get result")
    program_info['take_time'] = max_time
    program_info['take_memory'] = max_mem
    return program_info

