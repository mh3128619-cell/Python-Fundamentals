prices_USD = [10, 20, 30, 40, 50]
Exchange_Rate = float(input("Please, Enter the Exchange Rate: "))

prices_EGP = list(map(lambda num: num * Exchange_Rate, prices_USD))

print(f"The Exchange Rate is {Exchange_Rate}")
print("The prices in EGP are:", prices_EGP)
