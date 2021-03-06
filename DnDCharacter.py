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
class_mod = modifiers['class']
race_mod = modifiers['race']


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


class ModifyStats:
    modifier_strength = []
    modifier_dexterity = []
    modifier_constitution = []
    modifier_intelligence = []
    modifier_wisdom = []
    modifier_charisma = []


class HealthInfo:
    current_hitpoints = []
    max_hitpoints = []


class OtherInfo:
    armor_class = []
    initiative = []
    proficiency = []

#functions to access data from dict for use in main function
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

def menu():
    options = ('\033[1;33;40m-Options Menu-\n'
                'Please enter (1-6)\n'
                '\033[1;37;40m1. Character Info\n'
                '2. Character Stats\n'
                '3. Character Modifiers\n'
                '4. Characters Health\n'
                '5. Characters Other Info\n'
                '6. Exit\n'
                'Choice: ')
    choice = input(options)
    return choice


def search(items, search_value):
    for item in items:
        if item['friendlySubtypeName'] == search_value:
            return item['value']        
    return 0
    
         



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
    base_armor_class = 10

    
    race_modify_strength = search(race_mod, 'Strength Score')
    race_modify_constitution = search(race_mod, 'Constitution Score')
    race_modify_wisdom = search(race_mod, 'Wisdom Score')
    race_modify_dexterity = search(race_mod, 'Dextarity Score')
    race_modify_intelligence = search(race_mod, 'Intelligence Score')
    race_modify_charisma = search(race_mod, 'Charisma Score')

    
    class_modify_wisdom = search(class_mod, 'Wisdom Score')
    class_modify_charisma = search(class_mod, 'Charisma Score')
    class_modify_strength = search(class_mod, 'Strength Score')
    class_modify_dextarity = search(class_mod, 'Dextarity Score')
    class_modify_constitution = search(class_mod, 'Constitution Score')
    class_modify_intelligence = search(class_mod, 'Intelligence Score')

    unarmored_class_modifier = search(class_mod, 'Unarmored Armor Class')


    strength = totalStats(base_strength, race_modify_strength, class_modify_strength)
    dexterity = totalStats(base_dexterity, race_modify_dexterity, class_modify_dextarity)
    constitution = totalStats(base_constitution, race_modify_constitution, class_modify_constitution) 
    intelligence = totalStats(base_intelligence, race_modify_intelligence, class_modify_intelligence)
    wisdom = totalStats(base_wisdom, race_modify_wisdom, class_modify_wisdom)
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
    armor_class =  base_armor_class + modifier_dexterity + unarmored_class_modifier


    while True:
        choice = menu()
        if choice == '1':
            print('\033[1;31;40m-Here is the basic info-\n\033[1;37;40mCharacter Name:  \033[1;34;40m{}\n\033[1;37;40mCharacter Level:  \033[1;34;40m{}\n\033[1;37;40mCharacter Class:  \033[1;34;40m{}\n\033[1;37;40mCharacter Race:  \033[1;34;40m{}\n\033[1;37;40mGender:  \033[1;34;40m{}\n\033[1;37;40mAge:  \033[1;34;40m{}\n\033[1;37;40mMovement Speed:  \033[1;34;40m{}'.format(character_name, character_level, character_class, character_race, character_gender, character_age, base_speed))
        elif choice == '2':
            print('\033[1;31;40m-Here are the stats-\n\033[1;37;40mStrength: \033[1;34;40m{}\n\033[1;37;40mDexterity: \033[1;34;40m{}\n\033[1;37;40mConstitution: \033[1;34;40m{}\n\033[1;37;40mIntelligence: \033[1;34;40m{}\n\033[1;37;40mWisdom: \033[1;34;40m{}\n\033[1;37;40mCharisma: \033[1;34;40m{}'.format(strength, dexterity, constitution, intelligence, wisdom, charisma))
        elif choice == '3':
            print('\033[1;31;40m-Here are your Modifiers-\n\033[1;37;40mStrength: \033[1;34;40m{}\n\033[1;37;40mDexterity: \033[1;34;40m{}\n\033[1;37;40mConstitution: \033[1;34;40m{}\n\033[1;37;40mIntelligence: \033[1;34;40m{}\n\033[1;37;40mWisdom: \033[1;34;40m{}\n\033[1;37;40mCharisma: \033[1;34;40m{}'.format(modifier_strength, modifier_dexterity, modifier_constitution, modifier_intelligence, modifier_wisdom, modifier_charisma))
        elif choice == '4':
            print('\033[1;31;40m-here is the current/max hit points-\n\033[1;37;40mCurrent Hit Points: \033[1;34;40m{}\n\033[1;37;40mMax Hit Points: \033[1;34;40m{}'.format(current_hitpoints, max_hitpoints))
        elif choice == '5':
            print('\033[1;31;40m-Here is some other info-\n\033[1;37;40mArmor Class: \033[1;34;40m{}\n\033[1;37;40mInitiative: \033[1;34;40m{}\n\033[1;37;40mProficiency: \033[1;34;40m{}'.format(armor_class, initiative, proficiency))
        elif choice == '6':
            break
        else:
            print('\33[1;31;40m-You need to enter a number bewteen 1 and 6 please-')
            continue           



if __name__ == "__main__":
    main()