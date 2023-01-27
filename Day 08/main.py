from alphabet import alphabet
from caeser import caeser
from Utility.utility import continuity_check


total_alphabet = len(alphabet)
is_over = False

while not is_over:
    direction_control = False
    while not direction_control:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if direction == "encode" or direction == "decode":
            direction_control = True
        else:
            print("Type a valid input")
    text = input("Type your message: ").lower()
    shift_control = False
    while not shift_control:
        shift = int(input("Type the shift number: "))
        if shift < 0:
            print("Type a positive value")
        else:
            shift = shift % (total_alphabet // 2)
            shift_control = True
    result_text = caeser(text, shift, direction)
    print(f"The {direction + 'e'} text is: {result_text}")
    is_over = continuity_check(input("Do you want to continue? Yes or No "))
print("Thank you for using this chipher :)))))")
