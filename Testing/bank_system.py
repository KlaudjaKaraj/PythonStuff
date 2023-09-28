class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
        self.is_logged_in = False


class OnlineBank:
    def __init__(self):
        self.users = []

    def register(self, username, password):  # username is unique
        if not any((user for user in self.users if user.username == username)):
            self.users.append(User(username, password))
            return True
        return False

    def log_in_user(self, username, password):
        user = next((user for user in self.users if user.username == username), None)
        # another_user = [user for user in self.users if user.username == username]
        # print(user.username)
        # print(another_user[0].username)
        if user and user.password == password:
            user.is_logged_in = True
            return True
        return False

    def logout_user(self, username):
        user = next((user for user in self.users if user.username == username), None)
        if user:
            user.is_logged_in = False
            return True
        return False

    def is_user_logged_in(self, username):
        user = next((user for user in self.users if user.username == username), None)
        return user.is_logged_in if user else False

    def deposit(self, username, amount):
        user = next((user for user in self.users if user.username == username), None)
        if user and user.is_logged_in and amount > 0:
            user.balance += amount
            return user.balance
        return None

    def withdraw(self, username, amount):
        user = next((user for user in self.users if user.username == username), None)
        if user and user.is_logged_in and amount > 0 and user.balance >= amount:
            user.balance -= amount
            return user.balance
        return None