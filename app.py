import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))> 0:
        yn = input("Did you mean %s instead?" % get_close_matches(w,data.keys())[0]
        if yn == "Y":
            return
        elif yn == "N":
            return "The word doesn't exist"
    else:
        return "The word doesn't exist. Please double check."
word = input("Enter a word:")
print(dictionary(word))
