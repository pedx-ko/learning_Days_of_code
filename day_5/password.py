from random import randint, shuffle
import random



# Alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Symbols (Some common symbols)
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '?', '/', '>', '<', '.', ',', ';', ':', "'", '\"', '[', ']', '{', '}']

# Numbers (0-9)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


letters_to_select = 12  # here i can use a input for the user put his preferences
simbols_to_select = 9
numbers_to_select = 2


#bulding the paswword
passwos = []
for i in range(letters_to_select):
    # passwos.append(alphabet[randint(0,len(alphabet)-1)])
    passwos.append(random.choice(alphabet)) #choise is better for understanding code
    
for i in range(simbols_to_select):
    passwos.append(symbols[randint(0,len(symbols)-1)])
    
for i in range(numbers_to_select):
    passwos.append((numbers[randint(0,len(numbers)-1)]))

#ramdon order   
random.shuffle(passwos)

#converting to string for printing as a Password

passs = ""
for i in passwos:
    passs += str(i)
    # print(i)
print(passs)