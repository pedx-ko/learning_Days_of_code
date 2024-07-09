import os
import random
from time import sleep
from imagg import Intro_im

print(Intro_im)

List_of_participant = []
maximmales = 0
more_p = True
winner = ""
while more_p:
    participant = {}
    name = input("please put your name: ")

    trato = True
    while trato:
        try:
            bid = int(input("put you bid in numbers: "))
            # bid = random.randint(1, 500)
            trato = False
        except ValueError:
            print("Please provide a good data")
            sleep(1)
            os.system('cls')
    participant.update({"name": name, "bid": bid})
    List_of_participant.append(participant)

    trato = True
    while trato:
        respuesta = input("\nAre there more Bidders? Type 'yes' or 'no'\n")
        if respuesta == "yes" or respuesta == "no":
            trato = False
    if respuesta.lower() == "no":
        more_p = False
    os.system('cls')

    # print(f"\n\n{List_of_participant}\n\n")
for bides in List_of_participant:
    bids = bides["bid"]
    if bids > maximmales:
        maximmales = bids
        winner = bides["name"]

print(
    f"\n The winner is {winner.capitalize()} with the bid : {maximmales}$")
