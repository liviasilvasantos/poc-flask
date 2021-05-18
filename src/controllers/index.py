from flask import render_template
from src.app import application
from src.models.forms import LoginForm

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')


@application.route('/login', methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        print(form.remember_me.data)
    else:
        print(form.errors)

    return render_template('login.html', 
                        form=form)