success_number = 7
user_number = 0
tries = 10

while user_number != success_number and tries > 0:
    user_number = int(input("Please, Enter the guessing number: "))

    if user_number == success_number:
        print("You are right!")
        break
    else:
        tries = tries - 1
        if tries > 0:
            print(f"Invalid input, please try again. You have {tries} tries left.")
        else:
            print("Game over! You ran out of tries.")

else:
    if user_number == success_number:
        print("Thank you for playing!")
