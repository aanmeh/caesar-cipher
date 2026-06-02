# Caesar Cipher Tool

A command-line tool to encrypt and decrypt messages using the Caesar cipher.
Built as part of learning Python and cryptography fundamentals.

## What it does

- Encrypts a message by shifting each letter a chosen number of positions through the alphabet
- Decrypts a message back to plaintext using the same key
- Handles uppercase input, spaces, numbers, and punctuation

## How it works

Instead of shifting each letter one by one, the program builds an entirely new 
shifted alphabet and uses it as a lookup table. For example with a key of 3:

```
Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
Shifted:   d e f g h i j k l m n o p q r s t u v w x y z a b c
```

Every letter in the message is then swapped for its equivalent in the shifted alphabet.
Decryption works by shifting in the opposite direction using a negative key.

## How to run it

You'll be prompted to choose encrypt or decrypt, enter your message, and enter a key (any number from -26 to 26).

## Example

```
Do you want to Encrypt or Decrypt a message?: Encrypt
What is the message you want to encrypt: Hello World
What is the key (-26 to 26): 3
khoor zruog

Do you want to Encrypt or Decrypt a message?: Decrypt
What is the message you want to decrypt: khoor zruog
What is the key: 3
hello world
```

## What I learned

- How the Caesar cipher works and why it's vulnerable to brute-force attacks
- How to manipulate strings in Python using slicing (e.g. alphabet[key:] + alphabet[:key])
- How to handle edge cases like uppercase letters, spaces, and punctuation
- How encrypting and decrypting are really the same operation — just in opposite directions

## Why it matters

The Caesar cipher is one of the oldest encryption methods ever recorded, used by 
Julius Caesar himself. Understanding how it works, and how easily it can be broken 
— is a foundation for learning why modern encryption standards like AES exist and 
why key length and complexity matter in real security.
