from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import recipe_model
from flask import flash
from flask_bcrypt import Bcrypt
import re
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.recipes = []
        
    @classmethod
    def save(cls,user_data):
        query = """
                INSERT INTO 
                users
                (first_name, last_name, email, password)
                VALUES
                (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """
        return connectToMySQL(cls.db).query_db(query,user_data)

    @classmethod
    def get_by_email(cls,email):
        query = """
                SELECT * FROM users
                WHERE email = %(email)s;
                """
        results = connectToMySQL(cls.db).query_db(query,{'email':email})
        return cls(results[0]) if results else None
    
    @staticmethod
    def validate_registration(user):
        
        is_valid = True
        
        if User.get_by_email(user['email']) != None:
            is_valid = False
            flash('Email address already in use.', 'registration')
        
        if len(user['first_name']) < 2:
            is_valid = False
            flash('First Name must be at least 2 characters.', 'registration')
            
        if len(user['last_name']) < 2:
            is_valid = False
            flash('Last Name must be at least 2 characters.', 'registration')
            
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email.', 'registration')
            is_valid = False
            
        if len(user['password']) < 8:
            is_valid = False
            flash('Password must be at least 8 characters.', 'registration')
            
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash('Passwords do not match.', 'registration')
        
        return is_valid
