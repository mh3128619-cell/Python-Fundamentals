from math import *
destination = input("Enter your destination: ")
price = float(input("Enter your price: "))
tax = price * 0.15
total_price = ceil(price + tax)
print("Your destination is " + destination + " and the total price is " + str(total_price))
