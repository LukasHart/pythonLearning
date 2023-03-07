from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo_model, ninja_model

@app.route('/')
def index():
    all_dojos = dojo_model.Dojo.get_all_dojos()
    return render_template('index.html', all_dojos = all_dojos)

@app.route('/add/dojo',methods=["POST"])
def add_dojo():
    data = {
        'name':request.form['dojo_name']
    }
    dojo_model.Dojo.save_dojo(data)
    return redirect('/')

@app.route ('/view/dojo/<int:id>')
def view_dojo(id):
    data = {
        'id':id
    }
    ninjas = dojo_model.Dojo.get_ninjas_by_dojo(data)
    return render_template('view_one_dojo.html', dojos = ninjas)

@app.route('/delete/dojo/<int:id>')
def delete_dojo_by_id(id):
    dojo_model.Dojo.delete_dojo(id)
    return redirect('/')