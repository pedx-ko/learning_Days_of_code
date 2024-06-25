from time import sleep
import pretty_errors
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# modus = 1
# text = "el zapote es bueno par ala salud"
# text = "cj xynmrc cq zsclm nyp yjy qyjsb"
# shift = 2


# using the weaparound function to avoid error aout of range
def wraparound(index):
    return alphabet[index % len(alphabet)]

# index_to_lookup = 26  # an invalid index
# letter = wraparound(index_to_lookup)


# encoding
def encrypt(text=str, shift=int):
    mesage_enco = ""
    for te in text.lower():
        if te in alphabet:
            in_word = alphabet.index(te) + shift
            mesage_enco += wraparound(in_word)
        else:
            mesage_enco += te
    print(f"Encrypted message: \n{mesage_enco}")


# decoding
def decrypt(text_encoded=str, shift=int):
    mesage_enco = ""
    for te in text_encoded.lower():
        if te in alphabet:
            in_word = alphabet.index(te) - shift
            mesage_enco += wraparound(in_word)
        else:
            mesage_enco += te
    print(f"Nomarl message: \n{mesage_enco}")


# conditions to look wich one must
gain = True
asking = True
# while gain:
while asking:
    modus = input(
        "Type 'encode' to encrypt, type number 'decode' to decrypt:\n").lower()
    if modus == "encode" or modus == "decode":
        # modus = int(modus)
        print(modus)
        print("please provide 1 if want to encode or '2' if want to decode\n")
        asking = False
        os.system('cls')
        inpus = True
        while inpus:
            try:
                shift = int(input("Type the shift number:\n"))
                inpus = False

                if modus == "encode":
                    text = input(
                        "Type your message for encrypting:\n").lower()
                    os.system('cls')
                    encrypt(text=text, shift=shift)
                    inpus = False
                if modus == "dencode":
                    text = input(
                        "Type your message for decrypting:\n").lower()
                    os.system('cls')
                    decrypt(text_encoded=text, shift=shift)
                    inpus = False
            except ValueError:
                print("Invalid input. Please try again.\n")
                sleep(3)
                os.system('cls')

    else:
        os.system('cls')
    otra = True
    while otra:
        try:
            agan = int(input("Try again '1' no '2'\n"))
            otra = False
            if agan == 1 or agan == 2:
                os.system('cls')
                if agan == 1:
                    asking = True
                elif agan == 2:
                    asking = False
            else:
                print("vaule must be '1' or '2'")
                otra = False
        except ValueError:
            print("\nplease give a good answer\n")
            sleep(3)
            os.system('cls')
