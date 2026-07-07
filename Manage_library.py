def manage_library(books, action, book_name):
    if action == "add":
        books.append(book_name)
        print(f"Success: Added {book_name}")
    elif action == "remove":
        if book_name in books:
            books.remove(book_name)
            print(f"Success: Removed {book_name}")
        else:
            print(f"Error: {book_name} not found in library.")
    return books

my_library = ["python", "java"]

print("--- Welcome to the Interactive Library System ---")

while True:
    print(f"\nCurrent Library: {my_library}")
    choice = input("What would you like to do? (add / remove / done): ").lower()

    if choice == "done":
        print("Goodbye!")
        break
    
    if choice in ["add", "remove"]:
        name = input("Enter the book name: ")
        my_library = manage_library(my_library, choice, name)
    else:
        print("Invalid choice, please try again.")
