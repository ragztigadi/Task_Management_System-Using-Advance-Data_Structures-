from Models.user import User

class User_Services:
    def __init__(self):
        self.users ={}

    def add_users(self, id, name, email):
        