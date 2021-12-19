import json
from random import randint
from enum import Enum
import src.scraper as scraper
import src.image_scraper as image_scraper


def Generate_Cheese():
    # gen random number for type of cheese
    with open("src/data/all_cheeses.txt", 'r') as infile:
        lines = infile.readlines()
        count = 0
        for line in lines:
            count += 1
        cheese_num = randint(0, count)
        selected_cheese = lines[cheese_num].strip()

    if cheese_num <= 167:
        type = "Hard Cheese"
    elif cheese_num <= 273:
        type = "Semi Hard Cheese"
    elif cheese_num <= 362:
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

# Generate_Cheese()
