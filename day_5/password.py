from random import randint, shuffle
import random
from textwrap import shorten



# Alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Symbols (Some common symbols)
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '?', '/', '>', '<', '.', ',', ';', ':', "'", '\"', '[', ']', '{', '}']

# Numbers (0-9)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


letters_to_select = 12
simbols_to_select = 9
numbers_to_select = 2

selecting_alp = alphabet[randint(0,len(alphabet)-1)]
selecting_sym = symbols[randint(0,len(symbols)-1)]
selecting_num = numbers[randint(0,len(numbers)-1)]


passwos = ""
for i in range(letters_to_select):
    so = (alphabet[randint(0,len(alphabet)-1)])
    passwos += so


for i in range(simbols_to_select):
    so =(symbols[randint(0,len(symbols)-1)])
    passwos += so
    
for i in range(numbers_to_select):
    so = str((numbers[randint(0,len(numbers)-1)]))
    passwos += so
    
print(passwos)