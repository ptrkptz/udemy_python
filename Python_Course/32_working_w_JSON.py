""" import requests
import pprint
r = requests.get("https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple")

r.status_code
r.text
type(r.text) """

#  seperate run
import json
import requests
import pprint
r = requests.get("https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple")

question = json.loads(r.text)
type(question)

pprint.pprint(question['results'][0]['category'])
pprint.pprint(question['results'][0]['question'])
pprint.pprint(question['results'][0]['correct_answer'])
pprint.pprint(question['results'][0]['incorrect_answers'])

print(" # # # # # # # # # # #")
person = {'Name':'John', 'Age':30}
person_json = json.dumps(person)

print(person_json)