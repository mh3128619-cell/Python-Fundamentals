balance = 1000

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew {amount}. Remaining balance is {balance}")
    else:
        print("Insufficient balance!")

withdraw(500)
withdraw(200)
