import json
import os

def fix_data(file_name):
    with open(file_name, "r") as f:
        a = "".join(f.readlines())
        fixed_data = ",".join(a.split(']['))
    with open(file_name, "w") as f:
        f.write(json.dumps(fixed_data))

def save_data(file_name, data):
    f = open(file_name, "r+")
    old_data = json.load(f) # return a list of data that was already in data.json
    old_data.extend(answers) # combine old data with the new data
    f.write(json.dumps(old_data))
    f.close()


user_input = True

questions = {
"Name" : "What is your name?  ",
"Age" : "How old are you?  ",
"Birthday" : "When is your birthday?  ",
"Home" : "Where is your hometown?  ",
"Favorite_icecream" : "What is your favorite flavor of icecream?  ",
}

answers = []

def saveResp():
    user_input2 = True
    response = {}
    for c, q in questions.items():
        response[c] = input(q)
    answers.append(response)
    while user_input2:
        ask = input ('\n'+"Would you like to view all entries?  ")
        if ask == "yes" or ask == "Yes":
            print (answers)
            user_input2 = False
        elif ask == "no" or ask == "No":
            user_input2 = False
        else:
            print ("Sorry, I don't understand")

while user_input:
    userInput = input('\n'+"Would you like to complete this survey?  ")
    if userInput == "yes" or userInput == "Yes":
        saveResp()
    elif userInput == "no" or userInput == "No":
        user_input = False
    else:
        print ("Sorry, I don't understand")


if os.path.isfile(answers.json):
    file = open ("answers.json", "r+")
    old_data = json.load(file)
    old_data.extend(answers)
    file.write(json.dumps(old_data))
    file.close()

else:
    file = open("answers.json", "w")
    file.write(json.dumps(data))
    file.close()

# # IF FILE EXISTS, JUST APPEND TO OLD DATA
# if os.path.isfile("data.json"):
#     f = open("data.json", "r+")
#     #m = json.dumps(f)
#     old_data = json.load(f) # return a list of data that was already in data.json
#     for d in old_data:
#         print(d)
#     #old_data.extend(data) # combine old data with the new data
#     f.write(json.dumps(data))
#     f.close()
#
# # FILE DOES NOT EXIST SO CREATE NEW FILE
# else:
#with open("data.json", "w") as f:
#    f.write(json.dumps(data))
