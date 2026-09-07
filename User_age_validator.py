def register_user():
    while True:
        try:
            age = int(input("Please, Enter your age: "))
            
            if 0 <= age <= 120:
                print("Your age has been recorded successfully.")
                break
            else:
                print("Error: Age must be between 0 and 120.")
                
        except ValueError:
            print("Error: You should enter only valid integers.")

register_user()
