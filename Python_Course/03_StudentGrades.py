grade1 = float(input("Grade of test 1: "))
grade2 = float(input("Grade of test 2: "))
absenses = int(input("Number of absenses: "))
total_classes = int(input("Total number of classes: "))

avg_grade = (grade1+grade2)/2
attendance = (total_classes - absenses) / total_classes

print("Avg grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round((attendance *100),2))+"%")

if (avg_grade >= 6 and attendance >=0.8):
    print("Student has been approved.")
elif(avg_grade < 6 and attendance <0.8):
    print("Student failed due to an avg grade lower than 6 and attendance below 80%")
elif(attendance >= 0.8):
    print("Student failed bc of poor scores")
else:
    print("Student failed due to lack of participation of less than 80%")