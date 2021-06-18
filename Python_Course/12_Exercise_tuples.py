month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
birthdate=input("Enter the date you were born [dd-mm-yyyy]")

monthIndex=int(birthdate[3:5]) - 1
print("You were born in "+month[monthIndex])
