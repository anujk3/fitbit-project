from flask import render_template
from . import fitbit


@fitbit.route('/')
def index():
    return render_template('fitbit/index.html')


@fitbit.route('/user/<username>')
def user(username):
    return render_template('fitbit/username.html', username=username)