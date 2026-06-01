# ceasar cipher 

def caesar_cipher(message, key): # this is the function, it asks the user for the message and the key
    alphabet = "abcdefghijklmnopqrstuvwxyz" # just a list of the alphabet, will be used later
    partOne = "" # establishes part one of the new alphabet
    partTwo = "" # establishes part two of the new alphabet 
    newAlphabet = "" # establishes the new alphabet

    if key == 0: # if the key is zero, then the alphabet will be the same, and by extention the message will be the same
        newAlphabet = alphabet
    if key > 0: # the below code essencially does the wrpaping around, given that the key is a number from 0 - 25
        partTwo = alphabet[:key] # part two becomes the first part of the original alphabet till the key
        partOne = alphabet[key:] # part one is th erest of the alphabet from the key
        newAlphabet = partOne + partTwo # makes the new alphabet by combining the two part
    else: # in the instance of a negative number 
        partTwo = alphabet[:(26 + key)]
        partOne = alphabet[(26 + key):]
        newAlphabet = partOne + partTwo
    
    encrypted = ""
    for char in message: # for each letter in the message, it will do this 
        if char == " ": # if the message just has a space, then it will be a space in the new mesage
            encrypted += " "
        else:
            for i in range(0, len(alphabet)): # checks the letter from the message agasint the original alphabet
                if char == alphabet[i]: # if it is the same letter
                    encrypted += newAlphabet[i] # assigns the new letter from the new alphabet using the same index from the orignal one

    print(encrypted)

caesar_cipher(input("What is the message you want to encrypt: "), int(input("What is the key: ")))




