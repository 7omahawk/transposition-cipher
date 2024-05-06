# making Transposition cipher encryption and decryption using python

import sys
import math
domain = 26
string = "abcdefghijklmnopqrstuvwxyz"

def writeByRow(key, userInput):
    userInput = userInput.replace(" ","")    # excluding space from the sentence
    sizeOfKey = len(str(key))   # column size
    sizeOfInput = len(userInput)
    
    numberOfRow = math.ceil(sizeOfInput / sizeOfKey) # row size
    totalLengthOfInput = sizeOfKey * numberOfRow

    # for padding
    if totalLengthOfInput != sizeOfInput:
        padding = totalLengthOfInput - sizeOfInput
        for i in range(padding):
            userInput = userInput + "z"

    matrix = [["" for space in range(sizeOfKey)] for space in range(numberOfRow)] # making matrix

    # entering every single value of input into matrix with padding
    for i in range(numberOfRow):
        for j in range(sizeOfKey):
            index = i * sizeOfKey + j
            if index < len(userInput):
                matrix[i][j] = userInput[index]

    print(matrix)

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
            writeByRow(key, userInput)

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