import random

def basic_stats():
    # keeping this here for learning experience
    # count = 0
    # rolls = []
    # while count < 6:
    #     stat_count = 0
    #     stats = []
    #     while stat_count < 4:
    #         stats.append(random.randint(1, 6)) # roll a d6 4 times
    #         stat_count += 1
    #     #uncomment to debug    
    #     #print(stats)
    #     stats.sort() # Sort low to high
    #     # print(stats)
    #     stats.pop(0) # Drop lowest
    #     # print(stats)

    #     rolls.append(sum(stats)) # add the three remaining rolls and add them to the list of stats
    #     count += 1
    #     rolls = sorted(rolls, reverse=True) # Sort stats descending for later assignmet
    # return rolls
    scores = []

    for i in range(1, 7):
        roll = sorted(list(random.randrange(1, 7) for i in range(4)), reverse=True) 
        stat = (sum(roll) - min(roll))
        scores.append(stat)
    return sorted(scores, reverse=True)

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


