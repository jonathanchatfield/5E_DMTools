import random

def basic_stats():
   
    scores = []

    for i in range(1, 7):
        roll = sorted(list(random.randrange(1, 7) for i in range(4)), reverse=True) 
        stat = (sum(roll) - min(roll))
        scores.append(stat)
    
    return sorted(scores, reverse=True)

  
    
# First Edition Rules Mod    
def basic_stats_1e():
    scores = []

    for i in range(1, 7):
        abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        roll = sorted(list(random.randrange(1, 7) for i in range(4)), reverse=True) 
        #print(roll)
        stat = (sum(roll) - min(roll))
        scores.append(stat)

    stats = list(zip(abilities, scores))
    return stats


def random_race():
    possible_races = ["Aarakocra", "Aasimar", "Bugbear", "Centaur",	"Changeling",
                      "Dragonborn", "Dwarf", "Elf", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin",
                      "Goliath", "Halfling", "Half-Elf", "Half-Orc", "Hobgoblin", "Human", "Kalashtar",
                      "Kenku", "Kobold", "Lizardfolk", "Loxodon", "Minotaur", "Orc", "Shifter", "Tabaxi", 
                      "Tiefling", "Tortle", "Triton", "Vedalken", "Warforged", "Yuan-Ti Pureblood"]
    race = random.choice(possible_races)
    return race
    

def random_class():
    possible_classes = ["Fighter", "Ranger", "Wizard", "Sorceror", "Warlock", "Rogue", "Monk",
                        "Artificer", "Bard", "Cleric", "Paladin", "Druid", "Barbarian"]
    chosen_class = random.choice(possible_classes)
    return chosen_class


