import lists_file
import random_generators
from time import sleep
import math
import racial_modifiers

character_name = input("By what name will your character be known? ")

print("You may choose from the following races:")
print(", ".join(lists_file.character_races_basic))

character_race = input("What race will your character be? ").lower()

print("Let's roll stats before choosing a class.\n")
your_roll = random_generators.basic_stats()
sleep(2)
print(f"You rolled: {your_roll} \n")

print("The following classes are available, which will you choose? ")
print(", ".join(lists_file.character_classes))

character_class = input("Enter your choice: ")
print('\n')

character_creation = {"Name": character_name,
                      "Race": character_race,
                      "Class": character_class}

print("Here is what you have so far: \n")

for key, value in character_creation.items():
    print(f"{key}: {value}")

# Ability Score dictionary for score assignment

ability_scores = {'Strength': None,
                  'Dexterity': None,
                  'Constitution': None,
                  'Intelligence': None,
                  'Wisdom': None,
                  'Charisma': None}

# TODO add the ability to import racial modifiers dictionary based on race selection
# Static Racial dictionary for testing
# dragonborn = {'Strength': 2,
#               'Dexterity': 0,
#               'Constitution': 0,
#               'Intelligence': 0,
#               'Wisdom': 0,
#               'Charisma': 1}


# A dictionary that will be populated by the calculation of post-racially modified ability scores
modifiers = {'Strength': None,
             'Dexterity': None,
             'Constitution': None,
             'Intelligence': None,
             'Wisdom': None,
             'Charisma': None}

# **some sort of error checking needs to go here**#
for ability in ability_scores:
    print(f"Scores left to assign:{your_roll}")
    score = int(input(f"which score would you like to assign to {ability}: "))
    ability_scores[ability] = score
    your_roll.remove(score)
# **some sort of error checking needs to go here**#

print("Assigning...")
sleep(2)
print()
print("Your ability scores have been assigned as: ")
for key, value in ability_scores.items():
    print(key, value)

sleep(2)
print()
print(f"As a {character_race} the following scores are modified ")

for key, value in getattr(racial_modifiers, character_race).items():
    if value != 0:
        print(f"{key} {value:+}")


print("Adding racial modifiers:")
sleep(2)

# look at the base ability_scores, check if it exists in racial modifiers for dragonborn, and add the values that are
# different
for key in ability_scores:
    if key in getattr(racial_modifiers, character_race):
        ability_scores[key] = ability_scores[key] + getattr(racial_modifiers, character_race)[key]
    else:
        pass

print()
print("Your racially modified scores are: ")
for key, value in ability_scores.items():
    print(key, value)

for key in ability_scores:
    if key in modifiers:
        modifiers[key] = math.floor((ability_scores[key] - 10) / 2)

sleep(2)
print()
print("Your ability modifiers are: ")
for key, value in modifiers.items():
    if value > 0:
        print(f"{key}: +{value}")
    else:
        print(f"{key}: {value}")
