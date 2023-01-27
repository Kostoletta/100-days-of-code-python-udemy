import os
def yes_or_no_check(response=""):
    if response == "yes" or response == "no":
        return False
    else:
        return True

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')