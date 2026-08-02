#this program shows if a student is passed or failed in physics

PhysicsMarks = float (input ( "Enter the marks of the student in Physics : "))

if PhysicsMarks > 100 or PhysicsMarks < 0:
    print( "Entered marks are Invalid")

elif PhysicsMarks >= 35  :
    print ( "Student is passed in Physics")

else :
    print(" Student is failed in Physics")