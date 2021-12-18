import json
from random import randint
from enum import Enum
import scraper

# gen random number for type of cheese
type_num = randint(0, 3)

if type_num == 0:
    file = "hard_cheeses.txt"
elif type_num == 1:
    file = "semi_hard_cheeses.txt"
elif type_num == 2:
    file = "semi_soft_cheeses.txt"
else:
    file = "soft_cheeses.txt"

with open("src/data/" + file, 'r') as infile:
    lines = infile.readlines()

    count = 0

    for line in lines:
        count+= 1
    cheese_num = randint(0, count)
    selected_cheese = lines[cheese_num].strip()

scraper.main(selected_cheese)

