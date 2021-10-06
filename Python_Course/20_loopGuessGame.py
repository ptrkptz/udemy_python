import random
number = random.randint(0,10)

guess=int(input("I'm thinking about a number.  What is your guess? "))

while True:
    if guess == number:
        break
    else:
        guess=int(input("Guess again: "))
print("You guess correctly it was ", number)
