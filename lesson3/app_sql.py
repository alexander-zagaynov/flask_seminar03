from flask import Flask
from Flask_lesson_03.lesson3.app_sql import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


app.route('/')
def index():
    return 'Hello'

@app.cli.command('init-db')
def init_db():
    db.crete_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)








