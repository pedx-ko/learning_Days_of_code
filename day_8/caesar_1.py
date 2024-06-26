from time import sleep
import pretty_errors
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# using the weaparound function to avoid error aout of range


def wraparound(index):
    return alphabet[index % len(alphabet)]
# funtion to encript text


def encryption(text=str, shift_Amound=int, modus=str):
    '''functions allow to encript a text'''
    mesage_enco = ""
    if modus == "decode":
        shift_Amound *= -1
    for te in text.lower():
        if te in alphabet:
            in_word = alphabet.index(te) + shift_Amound
            mesage_enco += wraparound(in_word)
        else:
            mesage_enco += te
    print(f"Your {modus} Message is: \n{mesage_enco}")


asking = True
while asking:
    modus = input(
        "\nType 'encode' to encrypt, type number 'decode' to decrypt:\n").lower()
    # try:
    if modus == "encode" or modus == "decode":
        # print(modus)
        print(
            "\nplease type 'encode' if want to encode or 'decode' if want to decode\n")
        asking = False
        os.system('cls')
        inpus = True
        while inpus:
            try:
                shift = int(input("\nType the shift number:\n"))
                inpus = False
                text = input(
                    "\nType your message for encrypting:\n").lower()
                os.system('cls')
                encryption(text=text, shift_Amound=shift, modus=modus)
                # inpus = False
            except ValueError:
                print("Invalid input. Please try again.\n")
                sleep(3)
                os.system('cls')
        otra = True
        # asking if want to keep going or stop
        while otra:
            try:
                agan = int(
                    input("\nWant to keep going ?: type '1' if YES or '2' if NO\n"))
                otra = False
                if agan == 1 or agan == 2:
                    os.system('cls')
                    if agan == 1:
                        asking = True
                    if agan == 2:
                        asking = False
                        print("Bye")
                else:
                    print("vaule must be '1' or '2'")
                    otra = False
            except ValueError:
                print("\nplease give a good answer\n")
                sleep(3)
                os.system('cls')
    else:
        os.system('cls')
