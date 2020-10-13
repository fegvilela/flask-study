from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fernanda'}
    posts = [
        {
            'author': {'username': 'Luciana'},
            'body': 'Dia maneiro aqui'
        },
        {
            'author': {'username': 'Isabela'},
            'body': 'The Avengers é maneiro!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
