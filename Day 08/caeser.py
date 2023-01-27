import string
from alphabet import alphabet
def caeser(text: string, shift: int, direction: string) -> string:
    result = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i not in alphabet:
            result += i 
        else:
            index = alphabet.index(i)
            next_pick = index + shift
            result += alphabet[next_pick]
    return result