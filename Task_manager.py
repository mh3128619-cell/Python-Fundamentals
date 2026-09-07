file_name = "tasks.txt"

def add_tasks():
    while True:
        try:
            with open(file_name, 'a') as file:
                task = input("Enter the new task: ")
                file.write(task + "\n")
                print("Task added successfully.")
            
            choice = input("Do you want to add another task? (yes/no): ").lower()
            if choice != 'yes':
                print("Exiting... Goodbye!")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def read_tasks():
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            if content:
                print("\nYour current tasks:")
                print(content)
            else:
                print("\nYour task list is empty.")
    except FileNotFoundError:
        print("\nNo tasks file found yet.")

read_tasks()
add_tasks()
