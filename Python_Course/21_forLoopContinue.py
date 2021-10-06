gmc_models = ["Sierra", "", "Yukon", "Envoy", "Terrain"]
delim = " - - - - - - - -"

for model in gmc_models:
    if model =="":
        continue
    else:
        print (model)

print(delim)

myString = "This is a string"
for char in myString:
    print(char)

print(delim)

for x in range(0,10):
    print(x)

print(delim)

person = {'Name':'Brin', 'Age':6,'Gender':'Female'}

for key in person:
    print(key,":",person[key])

print(delim)

blog_posts = {"Python":["Math", "http", "data type", ], "Javascript":["Namespace", "New function"]}

for category in blog_posts:
    print("Posts about ", category)
    for post in blog_posts[category]:
        print(post)
