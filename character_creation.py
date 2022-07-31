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


class Character:

    def __init__(self, charrace, charclass):
        self.charrace = charrace
        self.charclass = charclass

    def classrace(self):
        return f'{self.charrace} {self.charclass}'


grummel_rumblebelly = Character("Dwarf", "Barbarian")

print(grummel_rumblebelly.classrace())
print(Character.classrace(grummel_rumblebelly))





 
 