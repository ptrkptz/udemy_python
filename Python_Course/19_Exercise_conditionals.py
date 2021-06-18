print("This will calculate your BMI!")

height = float(input("Enter your height (in inches): "))
weight = float(input("Enter your weight (in lbs): "))

BMI = (weight/(height*height))*703

if (BMI <=18.5) :
    classification = "UNDERWEIGHT"
elif(BMI >18.5 and BMI<=24.9) :
    classification = "NORMAL"
elif(BMI >24.9 and BMI <=29.9) :
    classification = "OVERWEIGHT"
else :
    classification = "OBESITY"

print("Your BMI classification is ",classification," (BMI: ",round(BMI,2),")")
     
