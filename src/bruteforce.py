options = [
    "Shift cipher",
    "Monoalphabetic substitution cipher",
    "Complete table",
    "Double complete table"
]

def shift_cipher():
    return


print("")
print("Bruteforce KAB  Copyright (C) 2021  uhl1k (Roman Janků)")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under the conditions of GNU General Public License version 3.0")
print("")

cipher = input("Enter a cipher to bruteforce: ")

for option in options:
    print("[" + str(options.index(option)) + "] " + option)

print("")

while True:
    try:
        selected = int(input("Select a cipher to bruteforce: "))
    except:
        print("Use number to select a cipher to bruteforce.")
        continue

    if selected == 0:
        print(options[0] + ":")
        break

    elif selected == 1:
        print(options[1] + ":")
        break

    elif selected == 2:
        print(options[2] + ":")
        break;

    elif selected == 3:
        print(options[3] + ":")
        break

    else:
        print("Number is out of available range of 0 to " + str(len(options) - 1) + ".")
