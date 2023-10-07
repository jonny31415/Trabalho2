from User import User, login

def main():
    user_list: list[User] = []
    u1 = User("João", "Password", "admin")
    u2 = User("Maria", "Admin", "moderator")
    u3 = User("José", "123456", "user")
    u4 = User("Ana", "J*a4Y6)o@HjkL", "user")
    user_list.append(u1)
    user_list.append(u2)
    user_list.append(u3)
    user_list.append(u4)

    # Print user list
    print("User list:")
    for user in user_list:
        print(user)

    # Attempt to login as João
    username = "João"
    password = "Password"
    login_result = login(user_list, username, password)
    if login_result:
        print(f"Login as {username} successful!")
    else:
        print(f"Login as {username} failed!")

if __name__=="__main__":
    main()