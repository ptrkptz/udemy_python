data_valid = False
while data_valid == False:
    grade1 = input("Grade of test 1: ")
    try:
        grade1 = float(grade1)
    except:
        print("* ~ * Numbers only for Grade 1 * ~ * ") 
        continue
    if grade1 < 0 or grade1 > 100:
        print(" * * Grade 1 should be btw 0 and 100")
        continue
    else:
        data_valid = True   

data_valid = False
while data_valid == False:
    grade2 = input("Grade of test 2: ")
    try:
        grade2 = float(grade2)
    except:
        print("* ~ * Numbers only for Grade 2 * ~ * ")
        continue
    if grade2 < 0 or grade2 > 100:
        print(" * * Grade 2 should be btw 0 and 100")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_classes = input("Total number of classes: ")
    try:
        total_classes = int(total_classes)
    except:
        print("* ~ * Numbers only for Total Classes* ~ * ")
        continue
    if total_classes <= 0:
        print(" * * Number of classes need to be less than or equal to 0")
        continue
    else:
        data_valid = True
    

data_valid = False
while data_valid == False:
    absenses = input("Number of absenses: ")
    try:
        absenses = int(absenses)
    except:
        print("* ~ * Numbers only for Absenses * ~ * ")
        continue
    if absenses < 0 or absenses > total_classes:
        print(" * * Number of absenses cant be less than the zero or greater than total classes")
        continue
    else:
        data_valid = True

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