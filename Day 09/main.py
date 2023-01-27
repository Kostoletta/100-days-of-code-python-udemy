from importlib import import_module
import os
from logo import logo

print(logo)
print("Welcometo the blind auction program!")

do_continue = True

partecipants = {}

while do_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    partecipants[name] = bid
    continue_request_control = False
    while not continue_request_control:
        continue_request = input(
            "Are there any other bidders? Type 'yes or 'no'. ").lower()
        if continue_request == "yes" or continue_request == "no":
            continue_request_control = True
        else:
            print("Type a valid input")
    if continue_request == "no":
        do_continue = False
    os.system('cls' if os.name == 'nt' else 'clear')



max = 0
winner_name = ""
for i in partecipants:
    if partecipants[i] > max:
        max = partecipants[i]
        winner_name = i
print(f"The winner is {winner_name} with a bid of ${max}")
