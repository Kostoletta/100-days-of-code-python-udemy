from art import logo, vs
from data import data
from random import choice
from utility import clear


def check_guess(a, b, user_guess: str):
    """Return true if guess is correct"""
    user_guess = user_guess.lower()
    correct_guess = "a" if a["follower_count"] > b["follower_count"] else "b"
    return True if user_guess == correct_guess else False


def get_enemy(current):
    flag = True
    while flag:
        next_choice = choice(data)
        if next_choice != current:
            flag = False
    return next_choice


def play():
    score = 0
    gameover = False
    print(logo)
    current_choice = choice(data)
    print(
        f"Compare A: {current_choice['name']}, a {current_choice['description']}, from {current_choice['country']}.")
    while not gameover:
        print(vs)
        next_choice = get_enemy(current_choice)
        print(
            f"Against B: {next_choice['name']}, a {next_choice['description']}, from {next_choice['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        clear()
        print(logo)

        if check_guess(current_choice, next_choice, guess):
            score += 1
            print(f"You are right. Your score: {score}")

            # swapping current and next choice
            current_choice = next_choice
            print(
                f"Compare A: {current_choice['name']}, a {current_choice['description']}, from {current_choice['country']}.")

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            gameover = True


play()
