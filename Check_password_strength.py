def check_password_strength(password):
    has_upper = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True

    if len(password) < 8:
        return "Weak: Too Short"
    elif has_upper and has_digit:
        return "Strong"
    else:
        return "Medium: Needs uppercase and digits"

user_pass = input("Please, enter the password: ")
result = check_password_strength(user_pass)
print(result)
