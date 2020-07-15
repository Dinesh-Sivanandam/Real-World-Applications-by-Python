import json #Impot=rting the json module
from difflib import get_close_matches #Importing get_close_matches from difflib module

data = json.load(open("data.json")) #Loading the file using the json.load() function

def translate(w):  #Function for translate words to lowercase and get close matches words
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")  #getting the input from the user

output = translate(word) #Calling the function to get the meaning

if type(output) == list: #Checking if the output has more sentences and printing it
    for item in output:
        print(item)
else:
    print(output)