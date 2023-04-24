alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def caesar(message, shift_amount, direction_c):
    word = ""
    for i in range(0, len(message)):
        letter = alphabet.index(message[i])
        if direction_c == "encode":
            word += alphabet[letter + shift_amount]
        elif direction_c == "decode":
            word += alphabet[letter - shift_amount]
        else:
            print(f"There is no option '{direction_c}'")
    print(f"Here's the {direction_c}d result: {word}")


caesar(message=text, shift_amount=shift, direction_c=direction)
