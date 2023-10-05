# !/usr/bin/env python3

import hashlib
import re

# Encode string with SHA256
def sha256_encode(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password_hash = sha256_encode(password)
        self.role = None # "admin", "moderator", "user"
        self._filter_username()
    
    # Check if username has special characters
    def _filter_username(self):
        regex_forbidden_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex_forbidden_chars.search(self.username):
            raise ValueError("Username cannot have special characters!")
             

def main():
    u1 = User("João", "Password")
    print(u1._User__password_hash)

if __name__=="__main__":
    main()