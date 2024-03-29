import random
import lists_file


# First Edition Rules Mod
def basic_stats_1e():
    scores = []

    for i in range(1, 7):
        abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        roll = sorted(list(random.randrange(1, 7) for i in range(4)), reverse=True)
        # print(roll)
        stat = (sum(roll) - min(roll))
        scores.append(stat)

    stats = list(zip(abilities, scores))
    return stats


def basic_stats():
    scores = []

    for i in range(1, 7):
        roll = sorted(list(random.randrange(1, 7) for i in range(4)), reverse=True)
        stat = (sum(roll) - min(roll))
        scores.append(stat)

    return sorted(scores, reverse=True)


def random_race():
    race = random.choice(lists_file.character_races_basic)
    return race


def random_class():
    chosen_class = random.choice(lists_file.character_classes)
    return chosen_class
