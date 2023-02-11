from flask_app import app
from flask import render_template,redirect,request 
from flask_app.models.user_model import User


@app.route('/')
def all_users():
    users_list = User.get_all_users()
    return render_template('all_users.html', all_users = users_list)

@app.route('/create/user')
def create_user():
    return render_template('create_user.html')

@app.route('/process', methods=['POST'])
def form_submission():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')


@app.route('/display/user/<int:id>')
def show(id):
    data = {
        'id':id
    }
    return render_template('display_user.html', user=User.show(data)[0])

@app.route('/edit/user/<int:id>')
def edit_user(id):
    data = {
        'id':id
    }
    return render_template('edit_user.html', user=User.get_one(data)[0])

@app.route('/edit', methods=['POST'])
def edit_user_submission():
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/')
    