#!/usr/bin/env python
import os
from flask.ext.script import Manager, Shell, Server
from example import app
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0",port =8080))
manager.add_command("shell", Shell())
@manager.command
def createdb():
    from example.models import db
    db.create_all()
@manager.command
def retrivedb():
    from example.models import User,db
    i=1
    _offset=10*(i-1)
    print(_offset)
    users = User.query.order_by(User.score.desc(),User.guesses).offset(_offset).all()[:10]
    print(users)
@manager.command
def filldb():
    from example.models import User,db
    for i in range(10):
        user=User('Test'+str(i),10*i,i,'India')
        db.session.add(user)
    db.session.commit()
manager.run()