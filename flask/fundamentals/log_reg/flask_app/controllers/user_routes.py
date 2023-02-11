from flask import render_template,redirect,request,session
from flask_app.models import user_model
from flask_app import app



@app.route('/')
def index():
    return render_template('log_reg.html')


@app.route('/register', methods=['POST'])
def register_user():
    if not user_model.User.validate_register(request.form):
        return redirect('/')
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

@app.route('/success')
def success():
    user_id={
        'id':session['user_id']
    }
    return render_template('success.html', user=user_model.User.get_one_user(user_id))

@app.route('/logout')
def logout_user():
    session.clear()
    return render_template('log_reg.html')