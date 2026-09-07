def verify_age():
    user_input = input("Please, Enter your age: ")
    
    if not user_input.isdigit():
        raise TypeError("Age must be a number")
    
    age = int(user_input)
    
    if age < 18:
        raise ValueError("You must be at least 18 years old")
    elif age > 100:
        raise ValueError("Age cannot be greater than 100")
    else:
        print("Access Granted!")

try:
    verify_age()
except TypeError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
