# Generate 4 numbers between 1 and 6
# Append these numbers to a list
# Drop the lowest number

from hashlib import new
import random


# rolls = []

# for i in range(1, 7):
#     roll = [random.randrange(1, 6) for i in range(4)]
#     roll.sort(reverse=True)
#     print(roll)
#     roll.pop()
#     rolls.append(sum(roll))
    
    

# print(sorted(rolls, reverse=True))

scores = []

for i in range(1, 7):
    
    roll = sorted(list(random.randrange(1, 7) for i in range(4)), reverse=True) 
    #print(roll)
    stat = (sum(roll) - min(roll))
    scores.append(stat)

    #1E Ruleset
    abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
   
#print(scores)

stats = list(zip(abilities, scores))

print(stats)



    


