#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
# from .. import celery
import subprocess32

d = subprocess32.check_output(['ls', '-l'])
print type(d)
print d
