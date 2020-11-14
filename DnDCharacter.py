import requests
import json


# Creating classes for the diffrent types of character info
class CharInfo:
    character_name = []
    character_level = []
    character_class = []
    character_race = []
    character_gender = []
    character_age = []
    speed = []


class Stats: 
    strength = []
    dextarity = []
    constitution = []
    intelagence = []
    wisdom = []
    charisma = []


class HealthInfo:
    current_hitpoints = []
    max_hitpoints = []


class OtherInfo:
    armor_class = []
    initiative = []
    #proficiency = []
    

def proficiencyBonus():
    if character_level == 1 or 2 or 3 or 4:
            proficiency = 2
    elif character_level == 5 or 6 or 7 or 8:
            proficiency = 3
    elif character_level == 9 or 10 or 11 or 12:
            proficiency = 4
    elif character_level == 13 or 14 or 15 or 16:
            proficiency = 5
    elif character_level == 17 or 18 or 19 or 20:
            proficiency = 6
    else:
        proficiency = 7
    return proficiency


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
    base_dexterity = stats[1]['value']
    base_constitution = stats[2]['value']
    base_intelagence = stats[3]['value']
    base_wisdom = stats[4]['value']
    base_charisma = stats[5]['value']
    base_hitpoints = sheet['baseHitPoints']
    base_speed = race['weightSpeeds']['normal']['walk']
    base_armor_class = [10]
    removed_hitpoints = sheet['removedHitPoints']

    
    race_modify_dexterity = modifiers['race'][6]['value']
    race_modify_intelagence = modifiers['race'][5]['value']
    race_modify_charisma = modifiers['race'][4]['value']

    
    class_modify_wisdom = modifiers['class'][0]['value']
    class_modify_charisma = modifiers['class'][1]['value']
    unarmored_class_modifier = modifiers['class'][14]['value']


    strength = base_strength
    dexterity = base_dexterity + race_modify_dexterity
    constitution = base_constitution 
    intelagence = base_intelagence + race_modify_intelagence
    wisdom = base_wisdom + class_modify_wisdom
    charisma = base_charisma + race_modify_charisma + class_modify_charisma


    modifier_strength = (strength - 10) // 2 
    modifier_dexterity = (dexterity - 10) // 2
    modifier_constitution = (constitution - 10) // 2
    modifier_intelangence = (intelagence - 10) // 2
    modifier_wisdom = (wisdom - 10) // 2
    modifier_charisma = (charisma - 10) // 2


    character_name = sheet['name']
    character_level = classes_refine['level']
    character_class = main_class['name']
    character_race = race['fullName']
    character_gender = sheet['gender']
    character_age = sheet['age']
    max_hitpoints = base_hitpoints + character_level
    current_hitpoints = max_hitpoints - removed_hitpoints
    initiative = modifier_dexterity
    proficiency = proficiencyBonus()


    #code that has not yet been added
    #race_modify_strength = []
    #race_modify_constitution = []
    #race_modify_wisdom = []
    #class_modify_strength = []
    #class_modify_dextarity = []
    #class_modify_constitution = []
    #class_modify_intelagence = []

    print(character_name, proficiency)

if __name__ == "__main__":
    main()