import lists_file
import random_generators
import time
 

character_name = input("By what name will your character be known? ")


print("You may choosed from the following races:")
print(", ".join(lists_file.character_races_basic))

character_race = input("What race will your character be? ")

print("Let's roll stats before choosing a class.\n")
your_roll = random_generators.basic_stats()
time.sleep(2)
print(f"You rolled: {your_roll} \n")

print("The following classes are available, which will you choose? ")
print(", ".join(lists_file.character_classes))

character_class = input("Enter your choice: ")
print('\n')

character_creation = {"Name": character_name,
                      "Race": character_race,
                      "Stats": your_roll,
                      "Class": character_class}

print("Here is what you have so far: \n")
for key, value in character_creation.items():
    print(f"{key}: {value}")






