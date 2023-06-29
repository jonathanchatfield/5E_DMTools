import lists_file
import random_generators
from time import sleep
import math
import racial_modifiers

character_name = input("By what name will your character be known? ")

print("You may choose from the following races:")
print(", ".join(lists_file.character_races_basic))

# consider a way to gracefully handle user input
# taking into account the format of the racial_modifiers file
# and how the output is presented

# Add a try:except to ensure race is in list provided
character_race = input("What race will your character be? ").lower()


print("Let's roll stats before choosing a class.\n")
your_roll = random_generators.basic_stats()
sleep(2)
print(f"You rolled: {your_roll} \n")

print("The following classes are available, which will you choose? ")
print(", ".join(lists_file.character_classes))

# Add a try:except to ensure class is chosen from list provided
character_class = input("Enter your choice: ")
print('\n')

character_creation = {"name": character_name,
                      "race": character_race,
                      "class": character_class}

print("Here is what you have so far: \n")

for key, value in character_creation.items():
    print(f"{key}: {value}")

# ability score dictionary for score assignment

ability_scores = {'strength': None,
                  'dexterity': None,
                  'constitution': None,
                  'intelligence': None,
                  'wisdom': None,
                  'charisma': None}

# a dictionary that will be populated by the calculation of post-racially modified ability scores
modifiers = {'strength': None,
             'dexterity': None,
             'constitution': None,
             'intelligence': None,
             'wisdom': None,
             'charisma': None}

# If the score isn't in the list, ask again
for ability in ability_scores:
    while True:
        try:
            print(f"Scores left to assign:{your_roll}")
            score = int(input(f"Which score would you like to assign to {ability}: "))
            ability_scores[ability] = score
            your_roll.remove(score)
        except ValueError:
            print("That score isn't in the list, try again.")
            continue
        else:
            # was parsed successfully
            break


print("Assigning...")
sleep(2)
print()
print("Your ability scores have been assigned as: ")
for key, value in ability_scores.items():
    print(key, value)

sleep(2)
print()
print(f"As a {character_race} the following scores are modified ")

# using getattr(object, name) I am able to pull in the appropriate
# dictionary from the racial_modifiers file for use
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

# actually works!