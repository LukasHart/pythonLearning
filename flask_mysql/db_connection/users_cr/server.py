from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)


@app.route('/')
def landing():
    users = User.get_all()
    print(users)
    return render_template('read.html', all_users = users)

@app.route('/create_user')
def create_user():
    return render_template('create_user.html')


@app.route('/create', methods=['POST'])
def add_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/edit', methods=['POST'])
def aedit_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/show')
def show_user():
    users = User.get_all()
    return render_template('user.html', all_users = users)

@app.route('edit/user')
def edit_user():
    users = User.get_all()
    return render_template('edit_user.html', all_users = users)


if __name__ == '__main__':
    app.run(debug=True)
