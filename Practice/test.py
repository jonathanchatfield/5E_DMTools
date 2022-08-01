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
    
            

### Adding skill modifers ####   
print(rolls)
for roll in rolls:
        modifiers.append(math.floor((roll - 10) / 2))

modded_scores = zip(rolls, modifiers) 
# print(list(modded_scores))

for score,modifier in modded_scores:
    print(f"Your score is {score} with a modifier of {modifier}")



