#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models.user import User, Admin
from app import create_app, db

app = create_app('testing')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Admin=Admin)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade

    # migrate database to latest revision
    upgrade()


@manager.command
def run_local():
    app.run('0.0.0.0', port=5000)


if __name__ == '__main__':
    manager.run()
