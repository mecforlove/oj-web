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
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

    @classmethod
    def init_app(cls, app):
        pass


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/oj-web'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
                              'mysql://root:@localhost/oj-web'

    @classmethod
    def init_app(cls, app):
        pass


config = {
    'testing': TestingConfig,
    'production': ProductionConfig
}
