from src.utils.hashlib import verify, encode
from src.database.operations import get_user, add_user


class Authenticator:

    @staticmethod
    def login(username, password):
        user = get_user(username)
        # Check if the username and password are valid
        return verify(password, user['password'])

    @staticmethod
    def register(username, password, user_type):
        add_user({
            "username": username,
            "password": encode(password),
            "user_type": user_type
        })

    @staticmethod
    def get_current_user(username, password):
        user = get_user(username)
        # Check if the username and password are valid
        if verify(password, user['password']):
            return user
        else:
            return None
