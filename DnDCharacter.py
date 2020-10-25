from bs4 import BeautifulSoup
import requests


url = "https://www.dndbeyond.com/characters/6917300/sOurHm"

info = requests.get(url)

html = BeautifulSoup(info.txt, "html.parser")

strength = []
dextarity = []
constitution = []
intelagence = []
wisdom = []
charisma = []
current_hp = []
acrobatics = []
animal_handling = []
arcana = []
armor_class = []
athletics = []
deception = []
history = []
initiative = []
insight = []
intimidation = []
investigation = []
max_hp = []
medicine = []
nature = []
perception = []
performance = []
persuasion = []
proficiency = []
religion = []
sleight_of_hand = []
speed = []
stealth = []
survival = []


def main():
    print('Hello')

if __name__ == "__main__":
    main()