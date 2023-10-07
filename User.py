# !/usr/bin/env python3

import hashlib
import re

# Encode string with SHA256
def sha256_encode(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password_hash = sha256_encode(password)
        self.role = role # "admin", "moderator", "user"
        self._filter_username()
    
    # Check if username has special characters
    def _filter_username(self):
        regex_forbidden_chars = re.compile('[@_!#$%^&*()<>?/\\|}{~:;.,+=]')
        if regex_forbidden_chars.search(self.username):
            raise ValueError("Username cannot have special characters!")
    
    def __repr__(self):
        return f"Username: {self.username}\nRole: {self.role}\n"
    
    def check_credentials(self, username, password):
        if username == self.username and sha256_encode(password) == self.password_hash:
            return True
        return False

def login(user_list: list[User], username: str, password: str) -> bool:
    for user in user_list:
        if user.check_credentials(username, password):
            return True
    return False