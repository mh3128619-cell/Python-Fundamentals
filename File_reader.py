file_name = input("Please enter the file name: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Sorry, this file does not exist.")
finally:
    print("The inspection process has finished.")
