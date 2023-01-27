from utility import yes_or_no_check, clear
from art import logo
from random import choice
############### Blackjack Project #####################
############### Our Blackjack House Rules #############

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


def compare_score(user, dealer):
    """Takes two scores and return the winner.
    0 -> user win, 1 -> dealer win, 2 -> user win - opponent over, 3 -> dealer win - user over , 4 -> user black jack, 5 -> dealer black jack, 6 -> draw"""
    win_statements = {
        0: "You win",
        1: "Dealer win",
        2: "You win, opponent went over",
        3: "Dealer win, you went over",
        4: "You win with a black jack",
        5: "Dealer win with a black jack",
        6: "Draw"
    }
    if user == dealer:
        r = 2
    elif user > 21:
        r = 3
    elif dealer > 21:
        r = 2
    elif user == 0:
        r = 4
    elif dealer == 0:
        r = 5
    elif user > dealer:
        r = 0
    else:
        r = 1
    return win_statements[r]


def calculate_score(cards: list) -> int:
    """Takes the list of card and calcualtes the score"""
    score = sum(cards)
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    return score


def deal_card():
    """Draws a card from the deck and returns it"""
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(card_deck)


og_str_request = f"Do you want to play a game of Blackjack? Type 'y' or 'n': "
og_str_request_fail = "Type a valid input "
keep_playing = True

play_choice = input(og_str_request)
while yes_or_no_check(play_choice):
    play_choice = input(og_str_request_fail)
keep_playing = True if play_choice == "y" else False

while keep_playing:
    print(logo)
    dealer_cards = []
    dealer_score = 0
    user_cards = []
    user_score = 0

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
    dealer_cards.append(deal_card())

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"\tYour cards: {user_cards}, your score: {user_score}")
        print(f"\tComputer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            str_request = f"Do you want to draw a new card? Type 'y' or 'n': "
            str_request_fail = "Type a valid input "
            user_new_pick = input(str_request)
            while yes_or_no_check(user_new_pick):
                user_new_pick = input(str_request_fail)
            if user_new_pick == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    print(f"\tYour final hand: {user_cards}, final score: {user_score}")

    while dealer_score < 17 and dealer_score != 0:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(
        f"\tComputers final hand: {dealer_cards}, final score: {dealer_score}")

    print(compare_score(user_score, dealer_score))

    play_choice = input(og_str_request)
    while yes_or_no_check(play_choice):
        play_choice = input(og_str_request_fail)
    keep_playing = True if play_choice == "y" else False
    clear()
