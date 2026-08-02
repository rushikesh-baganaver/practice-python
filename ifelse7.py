#This program is a basic calculator

num1 = float (input("Enter the first number : "))
op = input ( "Enter the operation :")
num2 = float (input("Enter the second number : "))

if op == "+" :
    print ("The addition of given numbers is :", num1+num2)

elif op == "-" :
    print ("the subtraction of given numbers is :", num1-num2)

elif op == "*" :
    print("the multiplication of given numbers is :", num1*num2)

elif  op == "/" : 
    if num2 == 0 :
        print ("not defined")

    else :
        print("the division of given numbers is :", num1/num2)

else :
    exit()






   

