from ast import Pass
from time import sleep
import pretty_errors  # noqa: F401
import os
from itertools import count
import random
from imagg import stages, Intro_im, game_over

again = 1
while again == 1:
    os.system('cls')  # Call the clear() function to clear the console
    print(Intro_im)
    words_list = ["mak", "silvester", "mari", "mar",
                  "apple", "banana", "cherry", "grape", "mango"]

    random_word = random.choice(words_list)
    # no_spaces = random_word.replace(" ", "")
    # random_word = words_list[3]
    spaces_on = len(random_word)
    lives_on = 6

    # TODO creating the spaces _
    spaces = ""
    for i in range(spaces_on):
        spaces += "_"

    # # TODO look if a letter--done
    # print("########### WELLL CCOOOMEE ########### \n")
    while lives_on > 0:
        # print()
        # print(random_word)
        print()
        input_word = input("\nSelect a word: ").lower()

        # print()
        # print(f"{spaces}\n")

        os.system('cls')  # Call the clear() function to clear the console
        # print(spaces.count("_"))

        # if spaces.count("_") > 0:
        if input_word not in spaces.lower():
            if input_word in random_word:
                for i in range(spaces_on):
                    if input_word == random_word[i].lower():
                        spaces = list(spaces)
                        spaces[i] = random_word[i]
                        # convert in to a strig to prin it
                        spaces = "".join([i for i in spaces])
                print(f"\n \n♥ LIvES ♥ = {lives_on} \n")
                if spaces.count("_") <= 0:
                    # Call the clear() function to clear the console
                    # os.system('cls')
                    print(spaces)
                    print("\nYOU Win\n")
                    break
                print(spaces)
            else:
                lives_on -= 1
                print(f"\n \n♥ LIvES ♥ = {lives_on}\n ")
                print(stages[lives_on])
                print(spaces)
        else:
            print("\n Is allready there try again")

    if lives_on <= 0:
        os.system('cls')  # Call the clear() function to clear the console
        print(stages[lives_on])
        print(game_over)
        # print("\n \n GAME OVER")
        print(f"\n \nThe words was: {random_word }")
    # sleep()
    trata = True
    while trata:
        choise = input("\nIf want to try again '1'  if not '0' \n")
        if choise == "1" or choise == "0":
            trata = False
        else:
            print("\n\nplease try to select a good answer \n\n")
            sleep(2)
            os.system('cls')  # Call the clear() function to clear the console
    again = int(choise)
