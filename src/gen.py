import json
from random import randint
from enum import Enum
import src.scraper as scraper
import src.image_scraper as image_scraper


def Generate_Cheese():
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

    if type_num == 0:
        type = "Hard Cheese"
    elif type_num == 1:
        type = "Semi Hard Cheese"
    elif type_num == 2:
        type = "Semi Soft Cheese"
    else:
        type = "Soft Cheese"

    cheese = {
        "name": selected_cheese,
        "type": type,
        "description": scraper.main(selected_cheese),
        "url": image_scraper.Image_Scrape(selected_cheese)
    }
    return cheese

#Generate_Cheese()

