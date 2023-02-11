from flask_app.config.myqlconnection import connectToMySQL

class Post:
    def __init__(self,data):
        self.id = data['id'],
        self.content = data['content'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.users = []