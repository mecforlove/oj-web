#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate

app = create_app('testing')
manager = Manager(app)
migrate = Migrate(app, db)


@manager.command
def profile(length=25, profile_dir=None):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
