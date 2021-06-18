person = {"name":"Patrick Peitz", "gender":"Male", "age": 44, "address": "Glenwood", "phone":40264704482}

userInput = input("What info would you like to see (name, gender, age, address, phone)? ").lower()

print ("Saved value is: " + person.get(userInput, "'"+userInput+"' not found"))
