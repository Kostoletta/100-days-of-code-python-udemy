from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_guess(guess, answer, lives):
    if guess == answer:
        print("You guessed the number!!")
    elif guess < answer:
        print("Too low")
        return lives - 1
    elif guess > answer:
        print("Too high")
        return lives - 1


def set_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return EASY_LEVEL if choice == "easy" else HARD_LEVEL


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # For debugging
    print(f"THE SOLUTION IS {answer}")
    # ^^^^^^^^^^^^^
    lives = set_difficulty()
    guess = None

    while guess != answer:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = check_guess(guess, answer, lives)

        if lives == 0:
            "You lost"
            return
        if guess != answer:
            print("Guess again")


game()
