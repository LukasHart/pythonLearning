from flask_bcrypt import Bcrypt
from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')
bcrypt = Bcrypt(app)


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated = data['updated_at']

    @classmethod
    def register_user(cls, data):
        hash_pword = bcrypt.generate_password_hash(data['password'])
        user_data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': hash_pword
        }
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        return connectToMySQL('log_reg_schema').query_db(query, user_data)

    @classmethod
    def get_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL('log_reg_schema').query_db(query, data)
        print(result)
        if len(result) < 1:
            return False
        one_user = cls(result[0])
        return one_user

    @classmethod
    def get_one_user(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('log_reg_schema').query_db(query, data)
        print(results)
        one_user = cls(results[0])
        return one_user

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash('First Name must be at least 2 characters')
            is_valid = False

        if len(data['last_name']) < 2:
            flash('last Name must be at least 2 characters')
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash('Please enter a valid email')
            is_valid = False

        if data['password'] != data['confirm_password']:
            flash('Passwords do not match')
            is_valid = False

        if not PASS_REGEX.match(data['password']):
            flash('your password is not strong enough!')

        if len(data['password']) < 8:
            flash('password must be at least 8 characters')
            is_valid = False

        return is_valid

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
