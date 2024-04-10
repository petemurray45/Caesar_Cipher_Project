alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
decipher_word = ""


def encrypt(phrase, iteration):
    cipher_text = ""

    for letter in phrase:
        position = alphabet.index(letter)
        new_position = position + iteration
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, new_iteration):
    deciphered_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - new_iteration
        deciphered_text += alphabet[new_position]
    print(f"The decoded text is {deciphered_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
