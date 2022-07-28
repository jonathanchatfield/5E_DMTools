import random_generators

for i in range(1, 1000):
    print(f"Your NPC is a/an: {random_generators.random_race()} {random_generators.random_class()}")
    print(f"Their stats are {random_generators.basic_stats()}")