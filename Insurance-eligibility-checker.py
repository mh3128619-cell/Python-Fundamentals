age = int(input("Enter your age: "))
accidents = int(input("Enter number of accidents: "))

if age < 18:
    print("Rejected - Age too young")
elif 18 <= age <= 25 and accidents > 2:
    print("Rejected - High risk")
elif age > 25 and accidents > 5:
    print("Rejected - Too many accidents")
elif 18 <= age <= 25 and accidents <= 2:
    print("Accepted - High premiums")
elif age > 25 and 1 <= accidents <= 5:
    print("Accepted - Medium premiums")
elif age > 25 and accidents == 0:
    print("Accepted - Low premiums")
