import os


def yes_or_no_check(response):
    if response == "y" or response == "n":
        return False
    else:
        return True


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
