from random_generators import basic_stats as stats
# generate scores

abilities_list = stats()


# assign scores to abilities dictionary within Character object

ability_scores  = {'Strength': 'Unassigned',
                   'Dexterity': 'Unassigned',
                   'Constitution': 'Unassigned',
                   'Intelligence': 'Unassigned',
                   'Wisdom': 'Unassigned',
                   'Charisma': 'Unassigned'}


### Strength
print(abilities_list)
strength_score = int(input("Which score would you like to assign to Strength? "))

ability_scores['Strength'] = strength_score

try:
    abilities_list.remove(strength_score)
except ValueError:
    print("Score not in list")

print(abilities_list)

### Dexterity

dexterity_score = int(input("Which score would you like to assign to Dexterity? "))

ability_scores['Dexterity'] = dexterity_score

try:
    abilities_list.remove(dexterity_score)
except ValueError:
    print("Score not in list")

print(abilities_list)

### Constitution

constitution_score = int(input("Which score would you like to assign to Constitution? "))

ability_scores['Constitution'] = constitution_score
try:
    abilities_list.remove(constitution_score)
except ValueError:
    print("Score not list")

print(abilities_list)

### Intelligence

intelligence_score = int(input("Which score would you like to assign to Intelligence? "))

ability_scores['Intelligence'] = intelligence_score

try:
    abilities_list.remove(intelligence_score)
except ValueError:
    print("Score not in list")

print(abilities_list)

### Wisdom

wisdom_score = int(input("Which score would you like to assign to Wisom? "))

ability_scores['Wisdom'] = wisdom_score

try:
    abilities_list.remove(wisdom_score)
except ValueError:
    print("Score not in list")

print(abilities_list)


### Charisma

charisma_score = int(input("Which score would you like to assign to Charisma? "))

ability_scores['Charisma'] = charisma_score

try:
    abilities_list.remove(charisma_score)
except ValueError:
    print("Score not in list")

print("Your base scores have been assigned as:")

for key, value in ability_scores.items():
    print(key, value)


class Character:
    
    def __init__(self, character_name, character_race, character_class, 
                 str_score, dex_score, con_score, int_score, wis_score, 
                 cha_score):
                 self.character_name = character_name
                 self.character_race = character_race
                 self.character_class = character_class
                 self.str_score = str_score
                 self.dex_score = dex_score
                 self.con_score = con_score
                 self.int_score = int_score
                 self.wis_score = wis_score
                 self.cha_score = cha_score

# Create the character based on user input
    @classmethod
    def character_input(cls):
               
        return cls(
            character_name = input("By what name shall you be known?: "),
            character_race = input("What is your Race?: "),
            character_class = input("What is your class?: "),
            str_score = ability_scores['Strength'],
            dex_score = ability_scores['Dexterity'],
            con_score = ability_scores['Constitution'],
            int_score = ability_scores['Intelligence'],
            wis_score = ability_scores['Wisdom'],
            cha_score = ability_scores['Charisma']
        )

    def display_character(self):
        print(f"""
        Character Name: {self.character_name}
        Character Race: {self.character_race}
        Character Class: {self.character_class}
        Strength: {self.str_score}   
        Dexterity: {self.dex_score}
        Constitution: {self.con_score}
        Intelligence: {self.int_score}
        Wisdom: {self.wis_score}
        Charisma: {self.cha_score}
        """)


character_1 = Character.character_input()
print(Character.display_character(character_1))





