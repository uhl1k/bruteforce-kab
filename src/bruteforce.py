import itertools


#  Ciphers that the program can decipher
options = [
    "Shift cipher",
    "Affine cipher",
    "Monoalphabetic substitution with keyword",
    "Vigenér cipher",
    "Complete table",
    "Complete table with keyword",
    "Double complete table"
]

alphabet = list("abcdefghijklmnopqrstuvwxyz")


#  Method for deciphering the simple shift cipher
def shift_cipher(cipher):
    try:
        #  Just cycle over all available shifts
        for i in range(0, len(alphabet)):
            result = ""
            for letter in list(cipher):
                result += alphabet[(alphabet.index(letter) - i) % len(alphabet)]
            print("[" + str((len(alphabet) - i) % len(alphabet)) + "]: " + result)
    except:
        print("Problem occurred when bruteforcing. Make sure cipher contains only letter from english alphabet.")


#  Method for deciphering
def monoalphabetic_cipher(cipher):
    try:
        #  Loop over all possible combinations of A and B
        for a in range(1, len(alphabet)):
            for b in range(len(alphabet)):
                #  Find the modulus multiplicative inverse
                a1 = 0
                for i in range(1, len(alphabet)):
                    if (i * a) % len(alphabet) == 1:
                        a1 = i
                        break
                #  Decipher the tex with given A and B
                result = ""
                for letter in list(cipher):
                    result += alphabet[(a1 * (alphabet.index(letter) - b)) % len(alphabet)]
                print("[a=" + str(a) + ";b=" + str(b) + "]: " + result)
    except Exception as ex:
        print("Problem occurred when bruteforcing. Make sure cipher contains only letter from english alphabet.")
        print(ex)


#  Method for monoalphabetic cipher with keyword
def monoalphabetic_with_keyword(cipher):
    length = 10
    try:
        length = int(input("Enter a maximum length of keyword (default is 10): "))
    except:
        length = 10

    for i in range(1, length):
        for key in itertools.product(alphabet, repeat=i):
            decipher = ""
            for letter in key:
                if letter not in decipher:
                    decipher += letter
            for letter in alphabet:
                if letter not in decipher:
                    decipher += letter
            result = ""
            for letter in cipher:
                result += alphabet[decipher.index(letter)]
            print("[key=" + "".join(map(str, key)) + "]: " + result)


#  -------------------------------  #
#  The main section of the program  #
#  -------------------------------  #

#  Print licensing information
print("")
print("Bruteforce KAB  Copyright (C) 2021  uhl1k (Roman Janků)")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under the conditions of GNU General Public License version 3.0")
print("")

#  Ask for a cipher to decipher
cipher = input("Enter a cipher to bruteforce: ").lower()

#  Print all available options
for option in options:
    print("[" + str(options.index(option)) + "] " + option)

print("")

while True:
    #  Ask user to select option
    try:
        selected = int(input("Select a cipher to bruteforce: "))
    #  User did not enter number
    except:
        print("Use number to select a cipher to bruteforce.")
        continue

    #  User selected a valid option
    if selected == 0:
        print(options[0] + ":")
        print("")
        shift_cipher(cipher)
        break

    elif selected == 1:
        print(options[1] + ":")
        print("")
        monoalphabetic_cipher(cipher)
        break

    elif selected == 2:
        print(options[2] + ":")
        print("")
        monoalphabetic_with_keyword(cipher)
        break

    #  user entered  number out of range
    else:
        print("Number is out of available range of 0 to " + str(len(options) - 1) + ".")
