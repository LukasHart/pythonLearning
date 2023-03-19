from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash

class Recipe:
    db = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.created_by = None
    
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO 
                recipes
                (user_id, name, description, instructions, date_cooked, under_30)
                VALUES
                (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s);
                """
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_recipe_by_id(cls,recipe_id):
        query = """
                SELECT * FROM recipes
                LEFT JOIN users 
                ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, {'id' : recipe_id})
        for row in results:
            recipe = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'password': '',
                'created_at':row['created_at'],
                'updated_at':row['updated_at']
            }
            recipe.created_by = user_model.User(user_data)
        return recipe
    
    @classmethod
    def get_all_recipes(cls):
        query = """
            SELECT * FROM recipes;
        """
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(result) for result in results]

    @classmethod 
    def get_users_recipes(cls):
        query = """
                SELECT * FROM recipes
                LEFT JOIN users
                ON recipes.user_id = users.id;
                """
        results = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        for row in results:
            one_recipe = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'password': '',
                'created_at':row['created_at'],
                'updated_at':row['updated_at']
            }
            recipe_creator = user_model.User(user_data)
            one_recipe.created_by = recipe_creator
            all_recipes.append(one_recipe)
        return all_recipes 

    @classmethod
    def edit_recipe(cls,data):
        query = """
                UPDATE recipes
                SET
                name = %(name)s,
                description = %(description)s,
                instructions = %(instructions)s,
                date_cooked = %(date_cooked)s,
                under_30 = %(under_30)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,id):
        query = """
                DELETE FROM recipes
                WHERE recipes.id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query, {'id': id})
    
    @staticmethod
    def validate_post(data):
        is_valid = True
        
        if len(data['name']) < 1:
            flash('Name must not be blank', 'post')
            is_valid = False
            
        if len(data['description']) < 1:
            flash('Description must not be blank', 'post')
            is_valid = False
            
        if len(data['instructions']) <1:
            flash('Instructions must not be blank', 'post')
            is_valid = False
            
        if data['date_cooked'] == '':
            flash('Date made must not be blank.', 'post')
            is_valid = False
            
        if 'under_30' not in data:
            flash('Under 30 must not be blank.', 'post')
            is_valid = False
        
        return is_valid