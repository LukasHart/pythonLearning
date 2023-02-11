from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo_model,ninja_model


@app.route('/dojos')
def index():
    dojo = dojo_model.Dojo.get_all_dojos()
    return render_template('/dojos.html', dojos = dojo)


@app.route('/new/dojo', methods=['POST'])
def new_dojo():
    data = {
        'name': request.form['name'],
        'location': request.form['location']
    }
    dojo_model.Dojo.save_dojo(data)
    return redirect('/dojos')


@app.route('/show/dojo/<int:id>')
def show_dojo(id):
    data = {
        'id':id
    }
    dojo = dojo_model.Dojo.get_ninjas(data)
    return render_template('show_dojo.html', dojo = dojo)