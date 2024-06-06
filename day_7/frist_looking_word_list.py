import pretty_errors  # noqa: F401
import os
from itertools import count
import random

words_list = ["mak silvester", "mari mar",
              "apple banana", "cherry", "grape mango"]

random_word = random.choice(words_list)
# no_spaces = random_word.replace(" ", "")
random_word = words_list[3]
spaces_on = len(random_word)
lives_on = 3

# TODO print this: _
spaces = ""
for i in range(spaces_on):
    spaces += "_"
print()
print(f"{spaces}\n")

# # TODO look if a letter--done
# print("########### WELLL CCOOOMEE ########### \n")
while lives_on > 0:
    print()
    print(random_word)
    print()
    input_word = input("\n select a word: ").lower()
    os.system('cls')  # Call the clear() function to clear the console
    if spaces.count("_") > 1:
        if input_word not in spaces.lower():
            if input_word in random_word:
                for i in range(spaces_on):
                    if input_word == random_word[i].lower():
                        spaces = list(spaces)
                        spaces[i] = random_word[i]
                        # convert in to a strig to prin it
                        spaces = "".join([i for i in spaces])
                print(f"\n \nlife = {lives_on} \n")
                print(spaces)
            else:
                lives_on -= 1
                print(f"\n \n life = {lives_on}\n ")
                print(spaces)
        else:
            print("\n Is allready there try again")
    else:
        print("Win")
        break

if lives_on <= 0:
    os.system('cls')  # Call the clear() function to clear the console
    print("\n \n GAME OVER")
print(f"\n \nThe words is: {random_word }")
