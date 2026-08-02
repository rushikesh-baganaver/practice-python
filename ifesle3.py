#This program is to show the largest of three numbers

num1 = int (input ("Enter the first Number : ") )
num2 = int ( input ( "Enter the second Number : "))
num3 = int ( input ( "Enter the third Number : "))

if num1 > num2 & num1 > num3 :
    print ( num1," is largest")

elif num2 > num3 & num2 > num1 :
    print ( num2,"is largest")

elif  num3 > num2 & num3 > num1 :
    print( num3, " is largest" )

else :
    print ( "Number is Invalid")