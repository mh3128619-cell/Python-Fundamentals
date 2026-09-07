import os

def read_file_data():
    file_path = input("Please, Enter the file path: ")
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist")
        
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                raise ValueError("The file is empty")
            else:
                print("File content:")
                print(content)
                
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file_data()
