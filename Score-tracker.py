total_score = 0

def add_score(points):
    global total_score
    total_score += points
    print(f"Your new total score is {total_score}")
    if total_score > 100:
        print(f"You have passed the test successfully, your score is {total_score}")
    else:
        print(f"You still need more points, your current score is {total_score}")

add_score(120)
add_score(60)
