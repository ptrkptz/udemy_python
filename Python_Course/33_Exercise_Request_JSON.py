import json
import requests
import pprint

print("We are going to play a trivia game.")
print("Game will continue until 'q' (quit) is typed.")

while True:
    r = requests.get("https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple")
    requestQuestion = json.loads(r.text)
    question = requestQuestion['results'][0]['question']
    pprint.pprint(question)

    others = []
    correct = requestQuestion['results'][0]['correct_answer']
    #others = requestQuestion['results'][0]['incorrect_answer']

    choices = []
    choices.append(correct)

    for x in requestQuestion['results'][0]['incorrect_answer']:
        print(x)
        choices.append(requestQuestion['results'][0]['incorrect_answer'][x])
    

    #pprint.pprint(requestQuestion['results'][0]['correct_answer'])
    #pprint.pprint(requestQuestion['results'][0]['incorrect_answers'])

    for y in choices:
        choices[y]

    print("")
    userContinue = input("Continue -- 'q' to quit, any key to see new question? ")


    if userContinue.lower() == 'q':
           break

print("Thanks for playing")