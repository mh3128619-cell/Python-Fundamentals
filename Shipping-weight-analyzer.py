from math import *

weight1 = abs(float(input("Enter the first weight: ")))
weight2 = abs(float(input("Enter the second weight: ")))
w1_ceil = ceil(weight1)
w2_ceil = ceil(weight2)

max_weight = max(w1_ceil, w2_ceil)
min_weight = min(w1_ceil, w2_ceil)
average = (w1_ceil + w2_ceil) / 2
root_average = sqrt(average)

print("--- Shipping Analysis---")

print("The maximum weight is: " + str(max_weight))
print("The minimum weight is: " + str(min_weight))
print("Square root of average weight is: ",root_average)
