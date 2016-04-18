#!/usr/bin/env python
import datetime
from flask_sqlalchemy import SQLAlchemy
from example import app
db=SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    score    = db.Column(db.Integer)
    guesses  = db.Column(db.Integer)
    country  = db.Column(db.String)
    def __init__(self,username,score,guesses,country):
        self.username = username
        self.score    = score
        self.guesses  = guesses
        self.country  = country