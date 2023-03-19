from flask_app import app
from flask_app.controllers import recipe_routes, user_routes
from flask import render_template,redirect,session

@app.route('/')
def reg_log():
    return render_template('reg_login.html')

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def invalid_request(e):
    return ('Please go back and enter a valid URL')

if __name__ == "__main__":
    app.run(debug=True)