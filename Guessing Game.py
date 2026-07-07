success_number = 7
user_number = 0

while user_number != success_number:
    user_number = int(input("Please, Enter the guessing number: "))
    
    if user_number == success_number:
        print("You are right!")
        break
    else:
        print("Invalid input, please try again.")
else:
    print("Thank you")
