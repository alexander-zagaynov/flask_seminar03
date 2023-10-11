from flask import Flask, render_template
import secrets

from models import db, Student, StudentMarks


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
app.config['DEBUG'] = True
app.config['SQLALGHEMY_DATABASE_URL'], = 'sqlite:///database.db'
db.init_app(app)
app.config.from_object(__name__)


@app.route('/')
def hello_world():
    return 'Hello world'


@app.cli.command('create=tables')
def create_tables():
    db.create_all()
    print('[+] OK')

@app.cli.command('fill-students-marks')
def fill_students_marks():
    for i in range(30):
        mark = StudentsMarks(student_id=random.randit(a:1, b:30), object_name=f'object{i}', object_mark=random.randit())
        db.session.add(mark)
    db.session.commit()

@app.route('/students/')
def show_students():
    students = db.StudentsMark.query.all()
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
