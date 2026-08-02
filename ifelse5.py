
TotalAverageMarks = float ( input( "Enter total average marks obtained by the student : "))

if TotalAverageMarks >= 91 and TotalAverageMarks <= 100 :
    print ( "You have obtained grade :'A'")

elif TotalAverageMarks >= 81 and TotalAverageMarks <= 90 :
    print ( "You have obtained grade :'B' ")

elif TotalAverageMarks >= 71 and TotalAverageMarks <= 80 :
    print ( "You have obtained grade :'C' ")

elif TotalAverageMarks >=61 and TotalAverageMarks <= 70 :
    print ( "You have obtained grade :'D'")

elif TotalAverageMarks >=51 and TotalAverageMarks <= 60 :
    print("You have obtained grade :'E'")

elif TotalAverageMarks >=35 and TotalAverageMarks <= 50 :
    print("You have obtained grade :'Pass'")

elif TotalAverageMarks < 35 and TotalAverageMarks >= 0 :
    print ("You have obtained grade :'F'\nYou have to reapear for the exam." )

elif TotalAverageMarks > 100 or TotalAverageMarks < 0 :
    print ("Invalid Total Average Marks")

else :
    print("Grade Not Availabe")