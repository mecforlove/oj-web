#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
import os


class Config(object):
    DEBUG = True
    TEST = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or "test"
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_RECYCLE = 30

    @classmethod
    def init_app(cls, app):
        pass


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/oj-web'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    @classmethod
    def init_app(cls, app):
        pass


config = {
    'testing': TestingConfig,
    'production': ProductionConfig
}
