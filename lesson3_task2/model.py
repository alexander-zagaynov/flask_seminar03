from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    student_marks = db.relationship('StudentsMarks', backref='student', lasy=True)


class StudentsMarks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoinsriment=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', nullable=False))
    object_name = db.Column(db.String, nullable=False)
    object_mark = db.Column(db.Integer, nullable=False)

