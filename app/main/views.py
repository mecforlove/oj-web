#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import render_template

from . import main


@main.route('/')
def index():
    return render_template('index.html')
