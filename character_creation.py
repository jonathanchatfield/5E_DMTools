# Create a class for each race
# Use the class to add relevant ability modifiers
#
#

# race
# class
# abilities
# ability modifiers
# proficiencies
# skills
# 


from email.errors import CharsetError


class Character:

    def __init__(self, character_name, character_race, character_class, str_score, dex_score, con_score, int_score, wis_score, cha_score):
        self.character_name = character_name
        self.character_race = character_race
        self.character_class = character_class
        self.str_score = str_score
        self.dex_score = dex_score
        self.con_score = con_score
        self.int_score = int_score
        self.wis_score = wis_score
        self.cha_score = cha_score

    def display_character(self):
        print()
        print(f"Character Name: {self.character_name}\nCharacter Race: {self.character_race} \nCharacter Class: {self.character_class} \nStrength: {self.str_score}\nDexterity: {self.dex_score}\nConstitution: {self.con_score}\nIntelligence: {self.int_score}\nWisdom: {self.wis_score}\nCharisma: {self.cha_score}\n")

    
    @classmethod
    def character_input(cls):
        return cls(
            character_name = input("By what name shall you be known?: "),
            character_race = input("What is your Race?: "),
            character_class = input("What is your class?: "),
            str_score = int(input("Enter your Strength Score: ")),
            dex_score = int(input("Enter your Dexterity Score: ")),
            con_score = int(input("Enter your Constitution Score: ")),
            int_score = int(input("Enter your Intelligence Score: ")),
            wis_score = int(input("Enter your Wisdom Score: ")),
            cha_score = int(input("Enter your Charisma Score: ")),
        )
            

Grummel = Character.character_input()
print(Character.display_character(Grummel))
