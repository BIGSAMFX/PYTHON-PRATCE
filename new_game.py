correct_username = "admin"
correct_password = "python123"
attempt = 0
limit = 3
while attempt < limit:
    username = input("Enter username: ")
    password = input("Enter password: ")
    attempt += 1
    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        print("Invalid login details")
else:
    print("Account locked")