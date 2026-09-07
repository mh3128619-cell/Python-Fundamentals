def withdraw():
  amount = float(input("Write your amount: "))
  balance = float(input("Write your balance: "))
  
  if amount > balance:
    raise ValueError(f"Insufficient Funds! Your balance is {balance} but you tried to withdraw {amount}")
  if amount <= 0:
    raise ValueError("Invalid withdrawal amount!")
  else:
    print(f"Withdrawal successful. Remaining balance is {balance - amount}")

try:
  withdraw()
except ValueError as e:
  print(f"Error: {e}")
