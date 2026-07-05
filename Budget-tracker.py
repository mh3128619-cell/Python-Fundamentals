total_budget = float(input("Please, Enter the total budget: "))
remaining_balance = total_budget
total_spent = 0

while remaining_balance > 0:
    user_input = input("Enter expense amount or type 'exit' to stop: ")

    if user_input.lower() == "exit":
        print(f"Program closed. Total spent: {total_spent}")
        break

    expense = float(user_input)
    
    if expense <= 0:
        print("Invalid input")
        continue

    remaining_balance -= expense
    total_spent += expense

    if remaining_balance <= 0:
        print(f"Remaining balance: {remaining_balance}")
        print("Budget exceeded! No more money left.")
        break
    else:
        print(f"Remaining balance: {remaining_balance}")
