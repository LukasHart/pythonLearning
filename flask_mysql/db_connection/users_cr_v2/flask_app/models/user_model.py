from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users_list = []
        for user in results:
            users_list.append(cls(user))
        return users_list
    
    @classmethod 
    def get_one(cls,id):
        query = 'SELECT * from users WHERE ID = %(id)s;'
        return connectToMySQL('users_schema').query_db(query,id)
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def show(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email= %(email)s, created_at = NOW(), updated_at = NOW() WHERE ID = %(id)s;'
        return connectToMySQL('users_schema').query_db(query,data)    