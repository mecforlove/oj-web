#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # register blueprints
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
