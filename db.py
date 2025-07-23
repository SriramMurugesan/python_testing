class Database:
    """Database class"""
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user):
        if user_id in self.users:
            raise ValueError("User already exists")
        self.users[user_id] = user
        return True

    def get_user(self, user_id):
        return self.users.get(user_id)

    def remove_user(self, user_id):
        if user_id not in self.users:
            raise ValueError("User does not exist")
        del self.users[user_id]
        return True

    def get_all_users(self):
        return self.users
