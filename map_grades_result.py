grades=[45,88,30,95,92]
for grade in list(map(lambda grade: "Success" if grade>=50 else "Fail",grades)):
  print(grade)
