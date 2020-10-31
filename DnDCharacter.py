from bs4 import BeautifulSoup
import requests


url = "https://www.dndbeyond.com/characters/6917300/sOurHm"

info = requests.get(url)

html = BeautifulSoup(info.txt, "html.parser")

class name:
    character_name = []
    character_lvl = []
    character_class = []
    character_race = []

class str: 
    strength = []
    athletics = []

class dex:
    dextarity = []
    acrobatics = []
    sleight_of_hand = []
    stealth = []

class con:
    constitution = []

class int:
    intelagence = []
    arcana = []
    history = []
    investigation = []
    nature = []
    religion = []

class wis:
    wisdom = []
    animal_handling = []
    insight = []
    medicine = []
    perception = []
    survival = []

class cha:
    charisma = []
    deception = []
    intimidation = []
    performance = []
    persuasion = []

class hp:
    current_hp = []
    max_hp = []

class other:
    armor_class = []
    initiative = []
    proficiency = []
    speed = []



def main():
    print('Hello World')

if __name__ == "__main__":
    main()