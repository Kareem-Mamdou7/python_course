def encrypt(plain_text, shift_amount):
    encrypted_text = ""

    for letter in plain_text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            encrypted_text += alphabet[new_index]

        else:
            encrypted_text += letter

    print(f"Encrypted message: {encrypted_text}")


alphabet = [chr(i) for i in range(97, 123)]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message:\n").lower()
shift = int(input("Type Shift Amount:\n"))

if direction == "encode":
    encrypt(text, shift)

elif direction == "decode":
    encrypt(text, -shift)
