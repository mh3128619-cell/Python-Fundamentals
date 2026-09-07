def register_user():
    username = input("Please, Enter your name: ")

    if len(username) < 5:
        raise ValueError("username must be at least 5 characters long")
    elif " " in username:
        raise ValueError("user name cannot contain spaces")
    else:
        print(f"{username} is successfully registered")

try:
    register_user()
except ValueError as e:
    print(f"Error: {e}")
