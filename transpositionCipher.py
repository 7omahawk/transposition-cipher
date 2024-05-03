# making Transposition cipher encryption and decryption using python

import sys
domain = 26
string = "abcdefghijklmnopqrstuvwxyz"

def makingRow(key, userInput):
    hi = "will be update soon"

def doingShuffle(key, userInput):
    hi = "will be update soon"

def encryption(key, userInput):
    hi = "will be update soon"




while(True):
    print("Enter your choice(Number): ")
    print("1. Encryption: ")
    print("2. Decryption: ")
    print("3. Exit: ")

    number = int(input("Enter the number: "))

    def choice(number):
        if number == 1:
            userInput = input("Enter your text to encrypt: ")
            key = int(input("Enter the key: "))
            userInput = userInput.lower()
            # encryption(userInput, key, domain, string)
        elif number == 2:
            userInput = input("Enter your text to decrypt: ")
            key = int(input("Enter the key: "))
            userInput = userInput.lower()
            # decryption(userInput, key, domain, string)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 