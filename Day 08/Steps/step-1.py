from caeser import decrypt, encrypt
from Utility.utility import continuity_check


do_continue = True
while do_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if(direction == "encode"):
        encrypt(text, shift)
    elif(direction == "decode"):
        decrypt(text, shift)

    do_continue = continuity_check(
        input("Do you want to continue? Yes or No "))