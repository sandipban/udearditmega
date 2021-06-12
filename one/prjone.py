import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff = 0.8)) > 0:
        yn =  input(f'Do you mean {get_close_matches(w, data.keys())[0].title()} instead? Press \"Y\" if yes or \"N\" to discontinue : ' )
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return 'The word does not exist, please recheck.'
        else:
            return 'We could not understand what you have written.'

    else:
        return 'Double check your spelling.'

word = input('Enter a word for meaning : ')

output = translate(word)
if isinstance(output, list):
# if type(output) == list :
    for items in output:
        print(items)
else:
    print(output)