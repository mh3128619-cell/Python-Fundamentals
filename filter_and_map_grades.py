grades = [45, 88, 30, 95, 52]
my_result = list(filter(lambda grade: grade >= 50, grades))
print(f"Passing grades: {my_result}")

def Evaluation():
  for result in map(lambda g: "Excellent" if g > 85 else "Good", my_result):
    print(result)

Evaluation()
