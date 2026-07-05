tasks = ["Study:Done", "Workout:Pending", "Read:Done", "Cook:Pending", "Clean:Pending"]

all_done = True

for i in tasks:
    if "Done" in i:
        continue
    else:
        print("You still need to do:", i)
        all_done = False

if all_done:
    print("Great job! All tasks are completed.")
