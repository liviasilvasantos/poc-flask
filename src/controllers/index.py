from flask import render_template
from src.app import application

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')


@application.route('/login')
def login():
    return render_template('base.html')