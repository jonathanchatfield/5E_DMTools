ability_scores  = {'Strength': 18,
                   'Dexterity': 10,
                   'Constitution': 11,
                   'Intelligence': 17,
                   'Wisdom': 13,
                   'Charisma': 11}

print(ability_scores)


dragonborn = {'Strength': 2,
              'Dexterity': 0,
              'Constitution': 0,
              'Intelligence': 0,
              'Wisdom': 0,
              'Charisma': 1}


# look at the base ability_scores, check if it exists in racial modifiers for dragonborn, and add the values that are different
for key in ability_scores:
    if key in dragonborn:
        ability_scores[key] = ability_scores[key] + dragonborn[key]
    else:
        pass
         
print(ability_scores)

