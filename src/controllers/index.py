from flask import render_template, flash, redirect, url_for
from src.app import application, db, loginManager
from src.models.forms import LoginForm
from src.models.tables import User
from flask_login import login_user, logout_user, login_required

@loginManager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

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
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Login OK!")
            return redirect(url_for('index'))
        else:
            flash("Invalid login")
    else:
        print(form.errors)

    return render_template('login.html', 
                        form=form)

@application.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@application.route("/create")
def create():
    user1 = User("livia", "1234", "Lívia Silva Santos", "liviasilvsantos@gmail.com")
    db.session.add(user1)
    user2 = User("rafael", "1234", "Rafael P Sousa", "rafaelps@gmail.com")
    db.session.add(user2)
    db.session.commit()
    return "Crud Ok!"

@application.route("/list")
def list():
    r = User.query.filter_by(username="livia").all()
    print(r)
    return "List Ok!"

@application.route("/update")
def update():
    r = User.query.filter_by(username="livia").first()
    r.email ="liviass@unicamp.br"
    db.session.add(r)
    db.session.commit()
    return "Update Ok!"

@application.route("/delete")
def delete():
    r = User.query.filter_by(username="rafael").first()
    db.session.delete(r)
    db.session.commit()
    return "Delete Ok!"