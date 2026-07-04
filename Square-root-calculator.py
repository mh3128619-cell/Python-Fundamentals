import math

number = float(input("Enter a number to get its root and ceil: "))
root = math.sqrt(number)
result = math.ceil(root)

print("The square root is: " + str(root))
print("The ceiling of the root is: " + str(result))
