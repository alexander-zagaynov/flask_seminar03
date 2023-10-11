import secrets
from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from sem_models import db, Student, Facultet
import random


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = secrets.token_hex()
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'
app.init_app(app)
db = SQLAlchemy(app)
app.config.from_object(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Index page'
    }
    return render_template('index.html', context=context)

@app.cli.command('create-tables')
def create_tables():
    db.create_all()
    print('[+] OK')


@app.cli.command('full-students')
def full_students():
    for i in range(10):
        students = Student(first_name=f'student{i}', last_name=f'last_name{i}', age=i+20, sex='male', group=500+i,
                           facultet_id=random.randint(1, 10))
    db.commit()


@app.cli.command('fill-facultet')
def fill_facultets():
    for i in range(10):
        facultet_name = Facultet(f'facultret{i}')
        db.session.add(facultet_name)
    db.session.commit()


@app.route('/students')
def show_all_students():
    students = Student.query.all()
    return render_template()


if __name__ == '__main__':
    app.run(debug=True)
