from time import sleep
import math
from random_generators import basic_stats as stats
# generate scores

abilities_list = stats()


# assign scores to abilities dictionary within Character object

ability_scores  = {'Strength': None,
                   'Dexterity': None,
                   'Constitution': None,
                   'Intelligence': None,
                   'Wisdom': None,
                   'Charisma': None}

dragonborn = {'Strength': 2,
              'Dexterity': 0,
              'Constitution': 0,
              'Intelligence': 0,
              'Wisdom': 0,
              'Charisma': 1}

modifiers = {'Strength': None,
                   'Dexterity': None,
                   'Constitution': None,
                   'Intelligence': None,
                   'Wisdom': None,
                   'Charisma': None}



for ability in ability_scores:
    print(abilities_list)
    score = int(input(f"which score would you like to assign to {ability}: "))
    ability_scores[ability] = score
    abilities_list.remove(score)

print()
print("Your ability scores have been assigned as: ")
for key, value in ability_scores.items():
    print(key,value)

print()
print("Adding racial modifiers...")
for key, value in dragonborn.items():
   if value != 0:
        if value > 0:
            print(f"{key} +{value}")
        else:
            print(f"{key} -{value}")
        sleep(3)
        
      
        
# look at the base ability_scores, check if it exists in racial modifiers for dragonborn, and add the values that are different
for key in ability_scores:
    if key in dragonborn:
        ability_scores[key] = ability_scores[key] + dragonborn[key]
    else:
        pass
         
print()
print("Your racially modified scores are: ")
for key, value in ability_scores.items():
    print(key,value)


for key in ability_scores:
    if key in modifiers:
        modifiers[key] = math.floor((ability_scores[key] - 10) / 2)


print()
print("Your ability modifiers are: ")
for key, value in modifiers.items():
    if value > 0:
        print(f"{key} + {value}")
    else:
        print(f"{key} {value}")





