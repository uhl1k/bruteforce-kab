#  Ciphers that the program can decipher
options = [
    "Shift cipher"
]


#  Method for deciphering the simple shift cipher
def shift_cipher(cipher):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(0, len(alphabet)):
        result = ""
        for letter in list(cipher):
            result += alphabet[(alphabet.index(letter) + i) % len(alphabet)]
        print("[" + str((len(alphabet) - i) % len(alphabet)) + "]: " + result)
    return


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
cipher = input("Enter a cipher to bruteforce: ")

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

    #  user entered  number out of range
    else:
        print("Number is out of available range of 0 to " + str(len(options) - 1) + ".")
