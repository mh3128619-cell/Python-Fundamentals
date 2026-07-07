def analyze_numbers_interactive():
    user_list = []
    
    while True:
        val = input("Enter a number (or type 'done' to finish): ")
        if val.lower() == 'done':
            break
        try:
            user_list.append(float(val))
        except ValueError:
            print("Please enter a valid number!")

    if not user_list:
        return "List is empty"

    results = {
        "sum": sum(user_list),
        "average": sum(user_list) / len(user_list),
        "max": max(user_list),
        "min": min(user_list)
    }
    
    return results

print(analyze_numbers_interactive())
