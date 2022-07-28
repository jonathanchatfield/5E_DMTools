import random_generators

print(f"Your NPC is a/an: {random_generators.random_race()} {random_generators.random_class()}")
print(f"Their stats are {random_generators.basic_stats()}")

# 1st Edition Ruleset
# stats = random_generators.basic_stats_1e()
# print("Their stats are:")
# for i, j in stats:
#     print(i, j)

# todo set up minimum stats for classes 