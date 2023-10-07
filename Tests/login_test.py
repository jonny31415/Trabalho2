from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from User import User, login
import pytest

user_list: list[User] = []
u1 = User("João", "Password", "admin")
u2 = User("Maria", "Admin", "moderator")
u3 = User("José", "123456", "user")
u4 = User("Ana", "J*a4Y6)o@HjkL", "user")
user_list.append(u1)
user_list.append(u2)
user_list.append(u3)
user_list.append(u4)

@pytest.mark.parametrize("username, password, expected", [("João", "Password", True), \
                                                          ("Maria", "Admin", True), \
                                                          ("José", "123456", True), \
                                                          ("Ana", "J*a4Y6)o@HjkL", True), \
                                                          ("João", "password", False), \
                                                          ("Maria", "admin", False), \
                                                          ("José", "1234567", False), \
                                                          ("Ana", "J*a4Y6)o@HjkL1", False)])
def test_user_login(username, password, expected):
    login_result = login(user_list, username, password)
    assert login_result == expected


@pytest.mark.parametrize("username, password", [("Jo@o", "Password"), \
                                                ("Maria#", "Admin"), \
                                                ("Jos=é", "123456"), \
                                                ("An|a", "J*a4Y6)o@HjkL"), \
                                                ("Joã(o", "password"), \
                                                ("Mar&ia", "admin"), \
                                                ("Jos%é", "1234567"), \
                                                ("Ana$", "J*a4Y6)o@HjkL1")])
def test_user_creation(username, password):
    with pytest.raises(ValueError):
        User(username, password, "user")