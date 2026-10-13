import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# Encrypt
plain_text = input("Enter a message to encrpyt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"orignal: {plain_text}")
print(f"encrypted: {cipher_text}")

# Decrypt
cipher_text = input("Enter a message to decrpyt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted: {cipher_text}")
print(f"orignal: {plain_text}")