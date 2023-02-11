from flask_app.config.myqlconnection import connectToMySQL
from flask_app import app
from flask import flash 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')

db = 'dojo_wall_schema'

class User:
    def __init__(self,data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.password = data['password'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
        
    @classmethod
    def register_user(cls,data):
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        return connectToMySQL(db).query_db(query,data)
    
    @classmethod
    def get_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL(db).query_db(query, data)
        print(result)
        if len(result) < 1:
            return False
        one_user = cls(result[0])
        return one_user
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_email = {
            'email': data['email']
        }
        user_exists = User.get_email(user_email)
        print(user_exists)
        if not user_exists:
            flash('Invalid email/password')
            is_valid = False
        if user_exists:
            if not bcrypt.check_password_hash(user_exists.password, data['password']):
                flash('Invalid email/password')
                is_valid = False
        return is_valid