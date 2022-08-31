import csv
import random
import os
import re

path = os.path.dirname(os.path.abspath(__file__))
file = '/pwd_hp.csv'

input_path = path + file

results = []
with open(input_path, newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row)

results = results[0]

def input_custom(list):
    maison = input('De quelle maison êtes-vous ?\n')
    prof = input('Quel est votre professeur(e) préféré(e) ?\n')
    sort_pref = input('Quel est votre sort préféré ?\n')
    patronus = input('Quel est votre patronus ?\n')
    l = []
    for sort in list:
        sort = sort + "_" + str(random.randint(0, 10000)) + maison + "_" + str(random.randint(0, 10000)) + prof + "__" + sort_pref + "_" + patronus + str(random.randint(0, 10000))

        # Modification des a/A en --> @
        sub = 'a'
        repl = '@'
        compiled = re.compile(re.escape(sub), re.IGNORECASE)
        sort = compiled.sub(repl, sort)

        # Modification des e/E en --> &
        sub = 'e'
        repl = '&'
        compiled = re.compile(re.escape(sub), re.IGNORECASE)
        sort = compiled.sub(repl, sort)

        # Modification des i/I en --> !
        sub = 'i'
        repl = '!'
        compiled = re.compile(re.escape(sub), re.IGNORECASE)
        sort = compiled.sub(repl, sort)

        # Supp spaces
        sort = sort.replace(' ', '')

        l.append(sort)
    return l


pwd_output = input_custom(results)

print(random.choice(pwd_output))


