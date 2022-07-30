# Generate 4 numbers between 1 and 6
# Append these numbers to a list
# Drop the lowest number

import random
import math

rolls = []
modifiers = []

for i in range(1, 7):
    roll = [random.randrange(1, 6) for i in range(4)]
    roll.sort(reverse=True)
    #print(roll)
    roll.pop()
    rolls.append(sum(roll))
    
            
   
print(rolls)
for roll in rolls:
        modifiers.append(math.floor((roll - 10) / 2))

modded_scores = zip(rolls, modifiers) 
# print(list(modded_scores))

for score,modifier in modded_scores:
    print(f"Your score is {score} with a modifier of {modifier}")



# scores = []

# for i in range(1, 7):
    
#     roll = sorted(list(random.randrange(1, 7) for i in range(4)), reverse=True) 
#     #print(roll)
#     stat = (sum(roll) - min(roll))
#     scores.append(stat)

#     #1E Ruleset
#     abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
   
# #print(scores)

# stats = list(zip(abilities, scores))

# print(stats)

# for i, j in stats:
#     print(i, j)



    


