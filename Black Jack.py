import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10]


answer = ()
player_hand = []
dealer_hand = []

accept = ["yes", "y"]
reject = ["no", "n"]
not_valid = ("\nThat is not a valid answer. Please respond with 'Y' or 'N'.")
print("\n\nWelcome to Blackjack! In this game the aim is to get to 21 or as close to 21 as possible without going over "
      "\nit. Whoever gets closer to or even gets 21 wins. If you both end up with the same score, it ends as a draw. "
      "\nGood Luck!")


def deal_player(player_hand):
    player_card = random.choice(deck)
    player_hand.append(player_card)
    return player_hand

def deal_dealer():
    dealer_hand = []
    while not (sum(dealer_hand) > 10):
        dealer_card = random.choice(deck)
        dealer_hand.append(dealer_card)
    return dealer_hand

def play():
    player_hand = []
    answer = ()
    deal_dealer()
    dealer_hand = deal_dealer()
    while answer not in reject:
        print("Your score is now", sum(player_hand))
        answer = input("\nWould you like to go again? Y/N \n>>> ").lower()
        if answer in accept:
            deal_player(player_hand)
            if sum(player_hand) == 21:
                print("Well Done! You got the exact score of ", sum(player_hand))
            elif sum(player_hand) >= 22:
                print("Uh Oh! You went bust. The dealer wins with a score of ", sum(dealer_hand))
        elif answer in reject:
            print("Your score was ", sum(player_hand))
            game_ended(player_hand, dealer_hand)
        else:
            print(not_valid)

def game_ended(player_hand, dealer_hand):
    #tells you the score of both dealer and user and who won or if they drew
    print("Your score is now ",sum(player_hand), "\nThe dealers score was ", sum(dealer_hand))
    if sum(dealer_hand) > sum(player_hand):
        print("\n\nThe dealer won")
    if sum(player_hand) > sum(dealer_hand):
        print("\n\nYou won!")
        play_again = input("Would you like to play again? Y/N \n>>> ").lower()
        if play_again in accept:
            play()
        else:
            print("Thank you for playing. I hope you enjoyed!")
    if sum(player_hand) == sum(dealer_hand):
        print("\n\nYou drew!")


play()