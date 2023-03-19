from flask_app import app
from flask_app.models import user_model,recipe_model
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/register', methods=["POST"])
def register():

    if user_model.User.validate_registration(request.form):

        user_model.User.save({
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        })
        
        flash('Thank you for registering', 'registration')
        
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    
    user = user_model.User.get_by_email(request.form['email'])
    
    if user == None or bcrypt.check_password_hash(user.password, request.form['password']) == False:
        flash('Invalid Credentials', 'login')
        return redirect('/')
    
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('dashboard.html', recipes = recipe_model.Recipe.get_users_recipes())