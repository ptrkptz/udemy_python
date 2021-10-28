import json
import requests
import random
import html

url = "https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple"
print("We are going to play a trivia game.")
print("Game will continue until 'q' (quit) is typed.")
print("")

score_correct = 0
score_incorrect = 0

continuePlaying = ""

while continuePlaying!='q':
    r = requests.get(url)
    if (r.status_code !=200):
        print("Error from the api, quitting!")
        userContinue = 'q'
    else:
        valid_Choice = False
        requestQuestion = json.loads(r.text)
        question = requestQuestion['results'][0]['question']
        correct = requestQuestion['results'][0]['correct_answer']
        others = requestQuestion['results'][0]['incorrect_answers']

        choices = []
        choices.append(correct)
        for i in others:
            choices.append(i)

        random.shuffle(choices)

    print(html.unescape(question)  + "\n")

    choiceNum = 0
    for choice in choices:
        choiceNum +=1
        print(str(choiceNum) + ": "+ html.unescape(choice))
        if choice == correct:
            correctNum = choiceNum

    while valid_Choice == False:
        userChoice = input("\nWhich number is your answer: ")
        try:
            userChoice = int(userChoice)
            if userChoice >len(choices) or userChoice<=0:
                print("Invalid answer")
            else:
                valid_Choice = True
        except:
            print("Invalid answer, only numbers allowed")

    if int(userChoice) == correctNum:
        print("You nailed it!!" + "\n")
        score_correct +=1
    else:
        print("Incorrect, the correct answer is: " + correct)
        score_incorrect +=1

    print("\n# # # # # # # # # # #")
    print("Running score -- correct: " +str(score_correct)+ " ~ incorrect: " +str(score_incorrect))
    print("# # # # # # # # # # #")

    continuePlaying = input("\nContinue? -- 'q' to quit, any key to see new question? ").lower()

print("\nThanks for playing")