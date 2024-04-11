alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
decipher_word = ""


def encrypt(code_text, code_iteration):
    cipher_text = ""

    for letter in code_text:
        position = alphabet.index(letter)
        new_position = position + code_iteration
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}")


def decrypt(code_text, code_iteration):
    deciphered_text = ""
    for letter in code_text:
        position = alphabet.index(letter)
        new_position = position - code_iteration
        deciphered_text += alphabet[new_position]

    print(f"The decoded text is {deciphered_text}")


def caesar(a, b, c):
    if c == "encode":
        encrypt(a, b)
    elif c == "decode":
        decrypt(a, b)


caesar(text, shift, direction)




