from langdetect import detect


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

#  Alphabetic with which the program works
alphabet = list("abcdefghijklmnopqrstuvwxyz")

#  Language that program should detect
lang = 'en'


#  Method for deciphering the simple shift cipher
def shift_cipher(cipher):
    try:
        solutions = list()
        #  Just cycle over all available shifts
        for i in range(0, len(alphabet)):
            decipher = ""
            for letter in list(cipher):
                decipher += alphabet[(alphabet.index(letter) - i) % len(alphabet)]
            solutions.append(("shift=" + str((len(alphabet) - i) % len(alphabet)), decipher))
        return solutions
    except Exception as e:
        print("Problem occurred when bruteforcing. Make sure cipher contains only letter from english alphabet.")
        print(e)


#  Method for deciphering affine cipher
def monoalphabetic_cipher(cipher):
    try:
        solutions = list()
        #  Loop over all possible combinations of A and B
        for a in range(1, len(alphabet)):
            for b in range(len(alphabet)):
                #  Find the modulus multiplicative inverse
                a1 = 0
                for i in range(1, len(alphabet)):
                    if (i*a) % len(alphabet) == 1:
                        a1 = i
                        break
                #  Decipher the tex with given A and B
                decipher = ""
                for letter in list(cipher):
                    decipher += alphabet[(a1 * (alphabet.index(letter) - b)) % len(alphabet)]
                solutions.append(("a=" + str(a) + ", b=" + str(b), decipher))
        return solutions
    except Exception as e:
        print("Problem occurred when bruteforcing. Make sure cipher contains only letter from english alphabet.")
        print(e)


#  Method for deciphering monoalphabetic substitution with key


#  Method for deciphering Vigenérs cipher

#  Method for decipher complete table
def complete_table(cipher):
    try:
        solutions = list()
        heights = list()
        for i in range(1, len(cipher) + 1):
            if (len(cipher) % i) == 0:
                heights.append(i)
        for height in heights:
            decipher = ''
            width = int(len(cipher) / height)
            for col in range(0, width):
                for line in range(0, height):
                    decipher += cipher[line*width + col]
            solutions.append((str(height) + 'x' + str(width), decipher))
        return solutions
    except Exception as e:
        print(e)


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
    solutions = list()
    if selected == 0:
        solutions = shift_cipher(cipher)

    elif selected == 1:
        solutions = monoalphabetic_cipher(cipher)

    elif selected == 4:
        solutions = complete_table(cipher)

    #  user entered  number out of range
    else:
        print("Number is out of available range of 0 to " + str(len(options) - 1) + ".")

    #  Print all solutions that might be english
    print()
    try:
        for solution in solutions:
            if detect(solution[1]) == lang:
                print(solution)
    except Exception as e:
        print(e)

    #  Does user want all solutions?
    print()
    if input("Do you want to print all solutions? [y/n]: ").lower() == 'y':
        print(solutions)

    break
