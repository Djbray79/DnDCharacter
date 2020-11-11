import requests
import json


# Creating classes for the diffrent types of character info
class CharInfo:
    character_name = []
    character_lvl = []
    character_class = []
    character_race = []
    character_gender = []
    character_age = []


class StrInfo: 
    strength = []
    #athletics = []


class DexInfo:
    dextarity = []
    #acrobatics = []
    #sleight_of_hand = []
    #stealth = []


class ConInfo:
    constitution = []


class IntInfo:
    intelagence = []
    #arcana = []
    #history = []
    #investigation = []
    #nature = []
    #religion = []


class WisInfo:
    wisdom = []
    #animal_handling = []
    #insight = []
    #medicine = []
    #perception = []
    #survival = []


class ChaInfo:
    charisma = []
    #deception = []
    #intimidation = []
    #performance = []
    #persuasion = []


class HealthInfo:
    current_hitpoints = []
    max_hitpoints = []


class OtherInfo:
    #armor_class = []
    #initiative = []
    #proficiency = []
    speed = []


def main():
    url = requests.get (
        "https://character-service.dndbeyond.com/character/v3/character/6917300"
        )

    page_dict = json.loads(url.text)

    sheet = page_dict['data']
    stats = sheet['stats']
    race = sheet['race']
    classes = sheet['classes']
    classes_refine = classes[0]
    main_class = classes_refine['definition']
    modifiers = sheet['modifiers']

    base_strength = stats[0]['value']
    base_dextarity = stats[1]['value']
    base_constitution = stats[2]['value']
    base_intelagence = stats[3]['value']
    base_wisdom = stats[4]['value']
    base_charisma = stats[5]['value']
    base_hitpoints = sheet['baseHitPoints']
    base_speed = race['weightSpeeds']['normal']['walk']
    removed_hitpoints = sheet['removedHitPoints']

    #race_modify_strength = []
    race_modify_dextarity = modifiers['race'][6]['value']
    #race_modify_constitution = []
    race_modify_intelagence = modifiers['race'][5]['value']
    #race_modify_wisdom = []
    race_modify_charisma = modifiers['race'][4]['value']

    #class_modify_strength = []
    #class_modify_dextarity = []
    #class_modify_constitution = []
    #class_modify_intelagence = []
    class_modify_wisdom = modifiers['class'][0]['value']
    class_modify_charisma = modifiers['class'][1]['value']

    character_name = sheet['name']
    character_level = classes_refine['level']
    character_class = main_class['name']
    character_race = race['fullName']
    character_gender = sheet['gender']
    character_age = sheet['age']
    max_hitpoints = base_hitpoints + character_level
    current_hitpoints = max_hitpoints - removed_hitpoints

    print(character_name, current_hitpoints)

if __name__ == "__main__":
    main()