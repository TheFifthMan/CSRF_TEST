from . import app,db
from app.models import User
from flask import render_template,request,url_for,flash,redirect
from flask_login import login_required,login_user,logout_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET',"POST"])
def login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            print('login successful')
            flash("You have login in and your name is {}".format(username))
            login_user(user)
            return redirect(url_for("index"))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/csrf',methods=['GET',"POST"])
@login_required
def csrf():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        u = User(username=username)
        u.password = password
        db.session.add(u)
        db.session.commit()
        flash('You have add a person.')
        return redirect(url_for('index'))

    return render_template('csrf.html')