try:
    USD_Amount = float(input("Please enter the USD Amount: "))
    Exchange_Rate = float(input("Please enter the Exchange Rate: "))

    if Exchange_Rate <= 0:
        raise ValueError("Exchange rate must be positive")
    
    Result = USD_Amount * Exchange_Rate

except ValueError as e:
    print(f"Error: {e}")

else:
    print(f"The result is: {Result}")

finally:
    print("The conversion system is ready for the next operation.")
