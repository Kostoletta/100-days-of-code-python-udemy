import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
ascii_art = [rock, paper, scissors]
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_choice < 0 or user_choice > 2:
    print("Chose a valid option")
else:
    print(ascii_art[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(ascii_art[computer_choice])
    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You brok the game somehow!!")
