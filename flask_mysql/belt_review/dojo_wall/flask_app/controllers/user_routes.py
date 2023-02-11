from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user_model

@app.route('/')
def index():
    return render_template('reg_log.html')

@app.route('/register', methods=['POST'])
def register_user():
    user_model.User.register_user(request.form)
    return redirect('/')

@app.route('/login', methods=['POST'])
def log_in_user():
    if not user_model.User.validate_login(request.form):
        return redirect('/')
    user_email={
        'email':request.form['email']
    }
    one_user=user_model.User.get_email(user_email)
    session['user_id']=one_user.id
    return redirect('/success')