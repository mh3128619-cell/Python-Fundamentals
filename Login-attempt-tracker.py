attempts = 0
max_attempts = 3

def login_attempt():
    global attempts
    attempts += 1
    
    if attempts >= max_attempts:
        print("System Locked: Too many failed attempts.")
    else:
        print(f"Login failed. Attempt {attempts} of {max_attempts}")

login_attempt()
login_attempt()
login_attempt()
