username = input("enter Username: ")
password = input(" enter Password: ")

if username!="admin" and password != "python123":
    print("username and password are incorrect")
elif username != "admin":
    print("invlid username")
elif password != "python123":
    print("invlid password")
else:
    print("login successful")



