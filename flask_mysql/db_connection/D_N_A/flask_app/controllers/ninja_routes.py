from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo_model, ninja_model

@app.route('/add/ninja')
def show_new_ninja_form():
    dojos_id = dojo_model.Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos = dojos_id)

@app.route('/add/ninja',methods=["POST"])
def save_ninja():
    ninja_model.Ninja.save_ninja(request.form)
    return redirect('/')

@app.route('/edit/ninja/<int:id>')
def edit_ninja_form(id):
    data = {
        'id':id
    }
    ninja = ninja_model.Ninja.get_ninjas_by_id(data)
    return render_template('edit_ninja.html', ninja = ninja)

@app.route('/edit/ninja', methods=['POST'])
def save_changes():
    ninja_model.Ninja.update_ninja(request.form)
    return redirect('/')

@app.route('/delete/ninja/<int:id>')
def delete_ninja(id):
    ninja_model.Ninja.delete_ninja_by_id(id)
    return redirect('/')