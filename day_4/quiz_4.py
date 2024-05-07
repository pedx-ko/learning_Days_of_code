'''
challenge interactive coding


create a script for mark spot on a map with an x
'''

#import the libray
from random import randint

#creating map grid
map = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Generate random vertical and horizontal coordinates within a 3x3 grid
vert = randint(0, 2)
hor = randint(0, 2)

# For testing purposes, uncomment the following lines to set fixed values
# vert = 1
# hor = 2

# User's guesses for vertical and horizontal coordinates
gesst__v = 1
gesst__h = 2

# Print the generated coordinates for reference
print(f'\nvertical : {vert} y Horizontal: {hor} ')

# Check if the user's guesses match the generated coordinates
if gesst__v == vert and gesst__h == hor:
    # If guesses are correct, mark the position with "O" on the map
    map[vert][hor] = "O"
    print("you win")
else:
    # If guesses are incorrect, mark the position with "x" on the map
    print("you lose, try again")
for i in map:
    print(i)