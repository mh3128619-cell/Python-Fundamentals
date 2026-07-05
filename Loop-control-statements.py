numbers = [10, 5, 20, 3, 15, 8, 7]

for i in numbers:
  
    if i == 15:
        break
  
    if i % 2 != 0:
        continue

    if i >= 10:
        print(i)
