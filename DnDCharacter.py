from bs4 import BeautifulSoup
import requests
import json



page = requests.get ("https://character-service.dndbeyond.com/character/v3/character/6917300")


sheet = BeautifulSoup(page.text, "html.parser")

print (sheet)



class Name:
    character_name = []
    character_lvl = []
    character_class = []
    character_race = []
    character_gender = []

class Str: 
    strength = []
    athletics = []

class Dex:
    dextarity = []
    acrobatics = []
    sleight_of_hand = []
    stealth = []

class Con:
    constitution = []

class Int:
    intelagence = []
    arcana = []
    history = []
    investigation = []
    nature = []
    religion = []

class Wis:
    wisdom = []
    animal_handling = []
    insight = []
    medicine = []
    perception = []
    survival = []

class Cha:
    charisma = []
    deception = []
    intimidation = []
    performance = []
    persuasion = []

class Hp:
    current_hp = []
    max_hp = []

class Other:
    armor_class = []
    initiative = []
    proficiency = []
    speed = []



def main():
    print('Hello World')

if __name__ == "__main__":
    main()