import requests
import json
import math


#import D&Dbeyond character json API and parse it
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
    intelligence = []
    wisdom = []
    charisma = []


class HealthInfo:
    current_hitpoints = []
    max_hitpoints = []


class OtherInfo:
    armor_class = []
    initiative = []
    proficiency = []

def proficiencyBonus(character_level):
    bonus = math.ceil(1 + (0.25 * (character_level)))
    return bonus

def totalStats(base, race, clas):
    total = base + race + clas
    return total

def getModifier(ability_score):
    modifier = (ability_score - 10) //2
    return modifier

def base_stats(base):
        base_score = stats[base]['value']
        return base_score

def race_modify(mod):
    race_modify = modifiers['race'][mod]['value']
    return race_modify

def class_modify(mod):
    class_modify = modifiers['class'][mod]['value']
    return class_modify


# this main function pulls down the character sheet and pulls out the relivant data
def main():

    base_strength = base_stats(0)
    base_dexterity = base_stats(1)
    base_constitution = base_stats(2)
    base_intelligence = base_stats(3)
    base_wisdom = base_stats(4)
    base_charisma = base_stats(5)


    base_hitpoints = sheet['baseHitPoints']
    removed_hitpoints = sheet['removedHitPoints']
    base_speed = race['weightSpeeds']['normal']['walk']
    base_armor_class = [10]

    
    race_modify_dexterity = race_modify(6)
    race_modify_intelligence = race_modify(5)
    race_modify_charisma = race_modify(4)

    
    class_modify_wisdom = class_modify(0)
    class_modify_charisma = class_modify(1)
    unarmored_class_modifier = class_modify(14)


    strength = totalStats(base_strength, 0, 0)
    dexterity = totalStats(base_dexterity, race_modify_dexterity, 0)
    constitution = totalStats(base_constitution, 0, 0) 
    intelligence = totalStats(base_intelligence, race_modify_intelligence, 0)
    wisdom = totalStats(base_wisdom, 0, class_modify_wisdom)
    charisma = totalStats(base_charisma, race_modify_charisma, class_modify_charisma)
        

    modifier_strength = getModifier(strength) 
    modifier_dexterity = getModifier(dexterity)
    modifier_constitution = getModifier(constitution)
    modifier_intelligence = getModifier(intelligence)
    modifier_wisdom = getModifier(wisdom)
    modifier_charisma = getModifier(charisma)


    character_name = sheet['name']
    character_level = classes_refine['level']
    character_class = main_class['name']
    character_race = race['fullName']
    character_gender = sheet['gender']
    character_age = sheet['age']
    max_hitpoints = base_hitpoints + character_level
    current_hitpoints = max_hitpoints - removed_hitpoints
    initiative = modifier_dexterity
    proficiency = proficiencyBonus(character_level)


    #code that has not yet been added
    #race_modify_strength = []
    #race_modify_constitution = []
    #race_modify_wisdom = []
    #class_modify_strength = []
    #class_modify_dextarity = []
    #class_modify_constitution = []
    #class_modify_intelligence = []

    print(character_name, class_modify_wisdom, race_modify_dexterity)

if __name__ == "__main__":
    main()