from time import sleep
import math
from random_generators import basic_stats as stats
import racial_modifiers

# generate scores
generated_scores = stats()
# chosen_race = racial_modifiers.dragonborn


# Ability Score dictionary for score assignment

ability_scores = {'Strength': None,
                  'Dexterity': None,
                  'Constitution': None,
                  'Intelligence': None,
                  'Wisdom': None,
                  'Charisma': None}

# TODO add the ability to import racial modifiers dictionary based on race selection
# Static Racial dictionary for testing
dragonborn = {'Strength': 2,
              'Dexterity': 0,
              'Constitution': 0,
              'Intelligence': 0,
              'Wisdom': 0,
              'Charisma': 1}

# A dictionary that will be populated by the calculation of post-racially modified ability scores
modifiers = {'Strength': None,
             'Dexterity': None,
             'Constitution': None,
             'Intelligence': None,
             'Wisdom': None,
             'Charisma': None}

for ability in ability_scores:
    print(generated_scores)
    score = int(input(f"which score would you like to assign to {ability}: "))
    ability_scores[ability] = score
    generated_scores.remove(score)

print("Assigning...")
sleep(2)
print()
print("Your ability scores have been assigned as: ")
for key, value in ability_scores.items():
    print(key, value)

sleep(2)
print()
print(f"As a Dragonborn the following scores are modified ")
for key, value in dragonborn.items():
    if value != 0:
        if value > 0:
            print(f"{key} +{value}")
        else:
            print(f"{key} -{value}")

print("Adding racial modifiers:")
sleep(2)

# look at the base ability_scores, check if it exists in racial modifiers for dragonborn, and add the values that are
# different
for key in ability_scores:
    if key in dragonborn:
        ability_scores[key] = ability_scores[key] + dragonborn[key]
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
