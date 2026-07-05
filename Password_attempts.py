correct_password = 1234
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = int(input("Please, Enter the password: "))
    
    if password == correct_password:
        print("Welcome to your account!")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")

else:
    print("Your card is blocked!")
