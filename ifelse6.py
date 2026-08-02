#this programs checks whether the username and password is correct or not?

username = input ( "Enter the username :")

if username != "admin" :
    print("Incorrect username")
else:
    Password = input("Enter the password :")
    
    if Password == "Python123" :
        print ( "Welcome to Your Dashboard")
    else :
        print ("Incorrect password")


