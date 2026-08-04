# A Mad Libs game is a word template game where one player asks another for random words like nouns or verbs without showing the story, then reads the final funny text aloud.
# You can build this in Python using basic features like the input() function, variables, and f-strings

name = input("Enter an alien name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective(description): ")
noun = input("Enter a noun(person,place,thing): ")
verb = input("Enter a verb(ending with ing): ")
exclamation = input("Enter an exclamation: ")

print(f"An alien named {name} landed in {place}.")
print(f"The creature looked extremely {adjective}.")
print(f"It carried a shiny {noun} everywhere.")
print(f"Suddenly, it began to {verb} wildly.")
print(f"It screamed '{exclamation}!' and flew away.")