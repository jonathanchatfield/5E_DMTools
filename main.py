from re import I
import random_generators
import lists_file


rollstats_answer = input("Would you like to roll your stats? ").lower()

if rollstats_answer == 'y':
    print(f"You rolled {random_generators.basic_stats()}")
else:
    print("Ok then, bye!")

assignstats_answer = input("Shall we assign your stats now? ").lower()

if assignstats_answer == 'y' or 'yes':
    






