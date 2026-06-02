# Caesar Cipher

def caesar_cipherEncrypt(message, key): # this is the function, it asks the user for the message and the key
    alphabet = "abcdefghijklmnopqrstuvwxyz" # just a list of the alphabet, will be used later
    message = message.lower() # converts the message to lowercase to handle uppercase input

    if key == 0: # if the key is zero, then the alphabet will be the same, and by extention the message will be the same
        newAlphabet = alphabet
    elif key > 0: # the below code essencially does the wrapping around, given that the key is a number from 0 - 25
        newAlphabet = alphabet[key:] + alphabet[:key] # makes the new alphabet by combining the two parts
    else: # in the instance of a negative number
        newAlphabet = alphabet[(26 + key):] + alphabet[:(26 + key)]

    encrypted = ""
    for char in message: # for each letter in the message, it will do this
        if char == " ": # if the message just has a space, then it will be a space in the new message
            encrypted += " "
        elif char not in alphabet: # if the character is not a letter (e.g. number or punctuation), keep it unchanged
            encrypted += char
        else:
            encrypted += newAlphabet[alphabet.index(char)] # assigns the new letter from the new alphabet using the same index from the original one

    print(encrypted)


def caesar_cipherDecrypt(message, key): # this is the decryption for a caesar cipher
    caesar_cipherEncrypt(message, (key - 2*key)) # simply uses the encryption method except the other way around, moving the letters in the opposite direction


def E_or_D():
    type = input("Do you want to Encrypt or Decrypt a message?: ")
    if type[0].lower() == "e":
        caesar_cipherEncrypt(
            input("What is the message you want to encrypt: "),
            int(input("What is the key (-26 to 26): "))
        )
    elif type[0].lower() == "d":
        caesar_cipherDecrypt(
            input("What is the message you want to decrypt: "),
            int(input("What is the key: "))
        )

E_or_D()
