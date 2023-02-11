from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import ninja_model,dojo_model


@app.route('/ninjas')
def add_ninja():
    dojo = dojo_model.Dojo.get_all_dojos()
    return render_template('create_ninja.html', dojos = dojo)

@app.route('/ninja/form', methods=['POST'])
def new_ninja_form():
    ninja_model.Ninja.save_ninja(request.form)
    return redirect('/dojos')

@app.route('/delete/<int:id>')
def delete_ninja(id):
    data = {
        'id':id
    }
    ninja_model.Ninja.delete_ninja(data)
    return redirect('/dojos')

@app.route('/edit/form', methods=['POST'])
def edit_user_form():
    data = {
        'id':request.form['id'],
        'dojo_id':request.form['dojo_id'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age']
    }
    ninja_model.Ninja.edit_ninja(data)
    return redirect('/dojos')

@app.route('/edit/user/<int:id>')
def edit_ninja(id):
    data = {
        'id':id
    }
    dojo = dojo_model.Dojo.get_all_dojos()
    return render_template('edit_ninja.html', ninja=ninja_model.Ninja.get_one_ninja(data),dojos=dojo)