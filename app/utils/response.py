#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec


def pagination_response(value, page, per_page, total):
    """生成分页响应"""
    return dict(
        code=0,
        msg='ok',
        data=dict(
            value=value,
            total=total,
            per_page=per_page,
            page=page
        )
    )


def common_response(code, msg):
    """普通响应"""
    return dict(
        code=code,
        msg=msg
    )


def data_response(data, code=0, msg='ok'):
    """返回单条信息的响应"""
    return dict(
        code=code,
        msg=msg,
        data=data
    )
