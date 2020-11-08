from flask import render_template
from microblog_app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Max'}
    posts = [
        {
            'author': {'username': 'User1'},
            'body': 'Test message 1!'
        },
        {
            'author': {'username': 'User2'},
            'body': 'Test message 2!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
