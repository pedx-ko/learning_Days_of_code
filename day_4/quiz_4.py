'''
challenge interactive coding


create a script for mark spot on a map with an x
'''

#import the libray
from random import randint
import os
from time import sleep

# #creating map grid

# map = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " "]
#     ]


def printmap(map):
    for i in map:
        print(i)
        
        
# Generate random vertical and horizontal coordinates within a 3x3 grid
# vert = randint(0, 2)
# hor = randint(0, 2)


## debigin
# machine = [randint(0, 2), randint(0, 2)]
# map[machine[0]][machine[1]]="x"

# printmap(map)


# For testing purposes, uncomment the following lines to set fixed values
# vert = 1
# hor = 2

again = True


# User's guesses for vertical and horizontal coordinates
while again:
    # again = True
    machine = [randint(0, 2), randint(0, 2)]
    # machine = [0, 2]
    map = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]
    print("\n\n\n Wellcome to the game")
    printmap(map)
    print()
    gesst__v = int(input("\nput in numbers the vertical point: ")) - 1
    gesst__h = int(input("put in numbers the horizontal point: ")) - 1
    # Print the generated coordinates for reference
    print(f'\nvertical : {machine[0] +1} y Horizontal: {machine[1] +1} ')

    # Check if the user's guesses match the generated coordinates
    if gesst__v == machine[0]and gesst__h == machine[1]:
        # If guesses are correct, mark the position with "O" on the map
        map[machine[0]][machine[1]]="0"
        print("    You WINN!!")
        printmap(map)
        again = False
    else:
        # If guesses are incorrect, mark the position with "x" on the map
        again = True
        print("you lose, try again\n")
        map[gesst__v][gesst__h] = "x"
        printmap(map)
    
        print("\nretraying ...")
        sleep(3)
        os.system('cls')# Call the clear() function to clear the console
        