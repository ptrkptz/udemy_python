import random

colors=["red", "blue", "orange", "black"]

while True:
        color = colors[random.randint(0,len(colors)-1)]
        guess = input("Guess color: ")

        while True:
            if (color == guess.lower()):
                break
            else:
                guess=input("Try again: ")

        print("Correct guess: ", color)

        play_again = input("Play again? N to quit ")

        if play_again.upper() == 'N':
           break
        
print("Thanks for playing")
