user_status="Guest"

def update_user():
    user_status="Admin"
    print(f"Print variable from function scope {user_status}")

update_user()
print(f"Print variable from global scope {user_status}")    
