# Generate 4 numbers between 1 and 6
# Append these numbers to a list
# Drop the lowest number

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
    
    roll = sorted(list(random.randrange(1, 6) for i in range(4)), reverse=True) 
    stat = (sum(roll) - min(roll))
    scores.append(stat)

print(scores)

    


