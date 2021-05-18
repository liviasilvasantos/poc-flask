from flask import render_template
from src.app import application, db
from src.models.forms import LoginForm
from src.models.tables import User


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

@application.route("/create")
def create():
    user1 = User("livia", "1234", "Lívia Silva Santos", "liviasilvsantos@gmail.com")
    db.session.add(user1)
    user2 = User("rafael", "1234", "Refael P Sousa", "rafaelps@gmail.com")
    db.session.add(user2)
    db.session.commit()
    return "Crud Ok!"

@application.route("/list")
def list():
    r = User.query.filter_by(username="rafael").all()
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