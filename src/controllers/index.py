from flask import render_template
from src.app import application

@application.route('/', defaults={"user":None})
@application.route('/index/<user>')
def index(user):
    return render_template('base.html', user=user)


@application.route('/login')
def login():
    return render_template('base.html')