from flask_sqialchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100)),
    last_name = db.Column(db.String(100), blank=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(100))
    group = db.Column(db.Integer)
    facultet_id = db.Column(db.Integer, db.ForeignKey('facultet.id'), nullable=False)

class Facultet(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    facultet_name = db.Column(db.String(100), nullable=False, uniuqe=True)
    students = db.relationship(*args: 'Student', backref='facultet')
