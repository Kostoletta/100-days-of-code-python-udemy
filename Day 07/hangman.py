import random
import os
from hangman_word import word_list
from hangman_art import logo, stages

print(logo + "\n")

chosen_word = random.choice(word_list)

# only for debug purpose
print(f"The chosen word is {chosen_word}")

display = ["_"] * len(chosen_word)

print(f"{' '.join(display)}")

guess_buffer = []
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Take a guess: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if "_" not in display:
        end_of_game = True
    if guess in guess_buffer:
        print(
            f"You have already guessed the letter {guess.upper()}, try another one")
    elif guess in chosen_word:
        for i in range(len(display)):
            if chosen_word[i] == guess:
                display[i] = guess
        guess_buffer.append(guess)
    else:
        print(f"The letter {guess.upper()} is not in the word")
        guess_buffer.append(guess)
        lives -= 1
    print(stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!!")
