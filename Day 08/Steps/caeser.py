alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    result = ""
    for i in text:
        index = alphabet.index(i)
        next_pick = index + shift
        while next_pick >= len(alphabet):
            next_pick -= len(alphabet)
        result += alphabet[next_pick]

    print(f"The enccoded text is {result}")


def decrypt(text, shift):
    result = ""
    for i in text:
        index = alphabet.index(i)
        next_pick = index - shift
        while next_pick < 0:
            next_pick += len(alphabet)
        result += alphabet[next_pick]
    print(f"The decoded text is {result}")