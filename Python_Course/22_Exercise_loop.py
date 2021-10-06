import random
names = []
number = random.randint(0,7)

for x in range(0,8):
    name = input("Enter name: ")
    names.append(name)


print("Random name: ", names[number])
