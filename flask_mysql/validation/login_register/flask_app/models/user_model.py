from flask_bcrypt import Bcrypt 
from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
import re
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')

class User:
    db = "log_reg"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO 
                users
                (first_name, last_name, email, password,created_at, updated_at)
                VALUES
                ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
                """
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_by_email(cls,email):
        query = """
                SELECT * FROM users
                WHERE email = %(email)s;
                """
        results = connectToMySQL(cls.db).query_db(query,email)
        return cls(results[0]) if results else None
    
    @classmethod
    def get_one(cls,data):
        query = """
                SELECT * FROM users
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0]) if results else None
    
    @staticmethod
    def validate_registration(user):
        is_valid = True
        
        if User.get_by_email(user['email']):
            is_valid = False
            flash('Email address already in use.', ' registration')
            
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email or Password', 'registration')
            is_valid = False
        
        if len(user['first_name']) < 3:
            is_valid = False
            flash('First Name must be at least 3 characters.', 'registration')
            
        if len(user['last_name']) < 3:
            is_valid = False
            flash('Last Name must be at least 3 characters.', 'registration')
            
        if len(user['password']) < 8:
            is_valid = False
            flash('Password must be at least 8 characters', 'registration')
            
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash('Passwords do not match.', 'registration')
        
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_email = {
            'email': data['email']
        }
        user_exists = User.get_by_email(user_email)
        print(user_exists)
        if not user_exists:
            flash('Invalid email/password')
            is_valid = False
        if user_exists:
            if not bcrypt.check_password_hash(user_exists.password, data['password']):
                flash('Invalid email/password')
                is_valid = False
        return is_valid               