numbers=[1,2,3,4,5]

for num in list(map(lambda num: (num/2) + (num%2), numbers)):
  print(num)
