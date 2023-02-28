from flask_app import app
from flask_app.models import user_model
from flask import render_template, redirect, request

@app.route('/')
def index():
    users = user_model.User.get_all_users()
    print(users)
    return render_template('read.html', users=users)

@app.route('/show_form')
def show_form():
    return render_template('create.html')

@app.route('/create', methods=["POST"])
def create():
    user_model.User.create_user(request.form)
    return redirect('/')