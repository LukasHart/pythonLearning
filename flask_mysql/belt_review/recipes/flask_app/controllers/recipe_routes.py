from flask_app import app
from flask_app.models import recipe_model
from flask import render_template,redirect,request,session

@app.route('/add/recipe')
def recipe_form():
    return render_template('add_recipe.html')

@app.route('/add/recipe', methods = ["POST"])
def save_recipe():
    
    if not recipe_model.Recipe.validate_post(request.form):
        return redirect('/add/recipe')
    
    recipe_data = {
        'user_id':session['user_id'],
        'name':request.form['name'],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'date_cooked':request.form['date_cooked'],
        'under_30':request.form['under_30']
    }
    
    recipe_model.Recipe.save(recipe_data)
    return redirect('/dashboard')

@app.route('/view/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    return render_template('view_recipe.html', recipe = recipe_model.Recipe.get_recipe_by_id(recipe_id))

@app.route('/edit/recipe/<int:recipe_id>')
def edit_form(recipe_id):
    return render_template('edit_recipe.html', recipe = recipe_model.Recipe.get_recipe_by_id(recipe_id))

@app.route('/edit/recipe', methods=["POST"])
def edit_recipe():
    recipe_id = request.form['id']
    if not recipe_model.Recipe.validate_post(request.form):
        return redirect(f'/edit/recipe/{recipe_id}')
    
    recipe_model.Recipe.edit_recipe(request.form)
    
    return redirect('/dashboard')

@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    recipe_model.Recipe.delete(id)
    return redirect('/dashboard')  