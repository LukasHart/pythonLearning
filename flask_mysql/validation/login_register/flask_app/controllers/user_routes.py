from flask import render_template, redirect, request, session, flash
from flask_app.models import user_model
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=["POST"])
def register():

    if user_model.User.validate_registration(request.form):

        user_id = user_model.User.save({
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        })
        flash('Thank you for registering')
        
        session['user_id'] = user_id
    return redirect('/')

@app.route('/login', methods=['POST'])
def log_in_user():
    if not user_model.User.validate_login(request.form):
        return redirect('/')
    user_email={
        'email':request.form['email']
    }
    one_user=user_model.User.get_by_email(user_email)
    session['user_id']=one_user.id
    return redirect('/success')

@app.route('/success')
def success():
    if not session:
        return redirect ('/')
    user_id = {'id':session['user_id']}
    return render_template('success.html', user = user_model.User.get_one(user_id))

@app.route('/logout')
def logout_user():
    session.clear()
    return render_template('index.html')

@app.errorhandler(404)
def invalid_request(e):
    return ('Please go back and enter a valid URL')
