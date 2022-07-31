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


from random_generators import basic_stats as stats


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

     
    @classmethod
    def character_input(cls):
        # Generate the 6 stat scores from the random_generator file
        # Create a list from those scores
        character_scores = stats()
        # Print the scores for debugging purposes
        print(character_scores)
        # Create the character based on user input
        # TODO have player CHOOSE where to place random scores

        return cls(
            character_name = input("By what name shall you be known?: "),
            character_race = input("What is your Race?: "),
            character_class = input("What is your class?: "),
            str_score = character_scores[0],#int(input("Enter your Strength Score: ")),
            dex_score = character_scores[1],#int(input("Enter your Dexterity Score: ")),
            con_score = character_scores[2],#int(input("Enter your Constitution Score: ")),
            int_score = character_scores[3],#int(input("Enter your Intelligence Score: ")),
            wis_score = character_scores[4], #int(input("Enter your Wisdom Score: ")),
            cha_score = character_scores[5],#int(input("Enter your Charisma Score: ")),
        )

    def display_character(self):
        print()
        print(f"Character Name: {self.character_name}\nCharacter Race: {self.character_race} \nCharacter Class: {self.character_class} \nStrength: {self.str_score}\nDexterity: {self.dex_score}\nConstitution: {self.con_score}\nIntelligence: {self.int_score}\nWisdom: {self.wis_score}\nCharisma: {self.cha_score}\n")           



character_1 = Character.character_input()
print(Character.display_character(character_1))
