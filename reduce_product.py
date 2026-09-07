from functools import reduce
numbers=[2,3,4,5]
result=reduce(lambda num1,num2:num1*num2,numbers)
print(result)
