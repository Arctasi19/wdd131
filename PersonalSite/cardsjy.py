import random

#IDEAS:
#use file writing to implement a scoreboard

DECKOFCARDS = [
    "Joker", "Joker", 
    "A-♠", "2-♠", "3-♠", "4-♠", "5-♠", "6-♠", "7-♠", "8-♠", "9-♠", "10-♠", "J-♠", "Q-♠", "K-♠",
    "A-♦", "2-♦", "3-♦", "4-♦", "5-♦", "6-♦", "7-♦", "8-♦", "9-♦", "10-♦", "J-♦", "Q-♦", "K-♦",
    "A-♥", "2-♥", "3-♥", "4-♥", "5-♥", "6-♥", "7-♥", "8-♥", "9-♥", "10-♥", "J-♥", "Q-♥", "K-♥",
    "A-♣", "2-♣", "3-♣", "4-♣", "5-♣", "6-♣", "7-♣", "8-♣", "9-♣", "10-♣", "J-♣", "Q-♣", "K-♣"
]
RANKMAPA14 = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
    "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14, "Joker": 0
}
RANKMAPA1 = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
    "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 1, "Joker": 0
}

TOTALGAMES = (2) + 1
TESTLIST = ["6-♣", "7-♣", "3-♣", "9-♣", "9-♣"]

def main():
    print("WELCOME TO TEXT-BASED-CARDS")
    print("Please select a game to play by entering its corresponding number:")
    print("1. Twenty-One (Blackjack)\n" 
    "2. Basic Poker")
    user_select = get_int("Please select a number: ", TOTALGAMES)
    if user_select == 1:
        twenty_one() #operational and finished
    elif user_select == 2:
        basic_poker() #operational. Missing a few features, but works in basic capacity.

# GAME MECHANIC COMPONENTS

def get_int(prompt,setrange=100): #COMPLETE
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in range(setrange):
                return user_input
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def get_str(prompt, expected_response_list): #COMPLETE
    while True:
        user_response = input(prompt)
        if user_response in expected_response_list:
            return user_response
        else:
            print("Please provide a valid input")

def deal_cards(current_deck, needed_cards): #COMPLETE
    #Takes remaining cards from the defined deck and "deals" a specified amount of cards
    #returns a list as the dealt hand
    cards = []
    for i in range(needed_cards):
        card_draw = random.choice(current_deck)
        cards.append(card_draw)
        current_deck.remove(card_draw)
    return cards

def compute_card_value(hand): #COMPLETE and Joker PROOF (only used in 21)
    value = 0
    for cards in hand:
        if cards != "Joker": #Jokers Don't Have Base Value
            cards.split("-")
            if cards[0] in ["J", "Q", "K", "10"]:
                value += 10
            elif cards[0] == "A":
                value += 11
            else:
                value += int(cards[0])
        else:
            continue
    return value

def hit_card(current_deck, hand): #COMPLETE
    user_hit_yn = input("Hit or pass? ").lower()
    if user_hit_yn == "pass":
        return False
    elif user_hit_yn == "hit":
        hand += deal_cards(current_deck, 1)
    else:
        print("Please enter 'hit' or 'pass'")

def discard_cards(list): #COMPLETE with Joker Functionality
    # remove cards from the hand list and deck, discarding them from the game.
    # TAKES A LIST
    # Displays a numbered contents of list
    # Have the user give a string containg the cards they want to discard
    # REMOVES CONTENTS OF LIST, ADDING THEM TO A DISCARD LIST
    # returns number of cards discarded
    hand = list
    discarded_list = []
    print("One at a time, enter the number value and suit of each card you want to discard.")
    print("Examples: '4 clubs' or 'king hearts'")
    while True:
        try: 
            target_card = []
            user_input = input("What card would you like to discard? (type 'cancel' to cancel discard) ")
            if user_input == "cancel":
                return "cancel"
            if user_input.lower() == "joker":
                removal_card == "joker"
            else:
                value, suit = user_input.split(" ")
                if value not in ["king", "queen", "jack", "ace", "joker"]:
                    target_card.append(str(value))
                elif value == "ace":
                    target_card.append("A")
                elif value == "king":
                    target_card.append("K")
                elif value == "queen":
                    target_card.append("Q")
                elif value == "jack":
                    target_card.append("J")

                if suit not in ["clubs", "hearts", "spades", "diamonds"]:
                    raise ValueError
                elif suit == "clubs":
                    target_card.append("-♣")
                elif suit == "hearts":
                    target_card.append("-♥")
                elif suit == "spades":
                    target_card.append("-♠")
                elif suit == "diamonds":
                    target_card.append("-♦")
                removal_card = ''.join(target_card)
            
            print(f"DISCARDED CARD: {removal_card}")
            if removal_card not in hand:
                raise IndexError
            else:
                list.remove(removal_card)
                discarded_list.append(removal_card)
                user_yn = get_str("Would you like to discard another card? (y/n) ", ["yes", "y", "no", "n"])
                if user_yn in ["yes","y"]:
                    continue
                else:
                    number_discarded = len(discarded_list)
                    return number_discarded
            
        except ValueError:
            print("ValueError in Discard Cards: Please enter a valid card.")
            print("Example: 'queen spades' or 'ace diamonds' or '5 clubs'")
        except IndexError:
            print("IndexError in Discard Cards: Card Entered Not In Hand")

def check_flush(list): #****COMPLETE Is in theory Joker Functional
    # Checks cards in a list to provide a boolean response to if the list contains a flush
    # TAKES A LIST
    # CHECKS THE SUIT OF EACH ITEM
    # IF ALL ITEMS ARE THE SAME SUIT, RETURN TRUE
    # ELSE, RETURN FALSE
    suit_list = []
    for card in list:
        if "-" in card:
            suit = card.split("-")[1]
            suit_list.append(suit)
    if len(suit_list) > 0 and all(s == suit_list[0] for s in suit_list):
        return True
    else:
        return False

def _can_form_straight(numerical_ranks, available_jokers): #HELPER FUNCTION for check_straight
    if not numerical_ranks: # If no actual cards in hand
        return available_jokers >= 5 

    unique_sorted_ranks = sorted(list(set(numerical_ranks)))
    if len(unique_sorted_ranks) != len(numerical_ranks):
        return False # Duplicate non-joker cards = no straight

    if len(unique_sorted_ranks) + available_jokers < 5:
        return False
        
    gaps_needed = 0
    for i in range(len(unique_sorted_ranks) - 1):
        diff = unique_sorted_ranks[i+1] - unique_sorted_ranks[i]
        if diff < 1: 
            return False 
        gaps_needed += (diff - 1)

    if available_jokers < gaps_needed: #check if there are enough jokers to fill gaps
        return False 

    remaining_jokers = available_jokers - gaps_needed

    # Check the potential straight span
    # A 5-card straight of any kind has a span of 4
    # The highest real card minus the lowest real card should be within a 'joker-assisted' span of 4
    
    # The highest value a straight could reach is lowest_card + 4
    # The lowest value a straight could reach is highest_card - 4

    # The maximum possible rank achievable by the last card in a 5-card straight
    # starting from unique_sorted_ranks[0] (lowest actual card) is unique_sorted_ranks[0] + 4.
    # If the last unique actual card is greater than this, it's too wide.
    if unique_sorted_ranks[-1] > (unique_sorted_ranks[0] + 4 + remaining_jokers):
        return False
        
    #Actual cards + remaining jokers must == 5
    
    # requirements:
    # if range (unique_sorted_ranks[-1] - unique_sorted_ranks[0]) plus the number of
    # "slots" filled by remaining_jokers == 4-slot difference:
    # Return True
    
    if (unique_sorted_ranks[-1] - unique_sorted_ranks[0]) <= (len(unique_sorted_ranks) + available_jokers - 1):
        return True
    
    return False

def check_straight(hand, jokercount): #COMPLETE and Joker functional
    non_joker_values_ace_high = [] # For checking Ace as 14
    non_joker_values_ace_low = []  # For checking Ace as 1 (if ace present)
    has_ace = False

    for card_str in hand:
        if card_str != "Joker":
            rank_str = card_str.split("-")[0]
            if rank_str == 'A':
                has_ace = True
                non_joker_values_ace_high.append(RANKMAPA14[rank_str]) # Ace as 14
                non_joker_values_ace_low.append(1) # Ace as 1
            else:
                value = RANKMAPA14[rank_str]
                non_joker_values_ace_high.append(value)
                non_joker_values_ace_low.append(value) # Same value for non-Ace cards

    # Scenario 1: Check for straight with Ace as 14 (or without an ace)
    if _can_form_straight(non_joker_values_ace_high, jokercount):
        return True

    # Scenario 2: If Ace was present, check for straight with ace as 1
    if has_ace:
        if _can_form_straight(non_joker_values_ace_low, jokercount):
            return True

    return False

def duplicate_dict_counter(list): #COMPLETE and Joker Functional
    # Takes a list and returns a dictionary with the count of each item
    # TAKES A LIST
    # RETURNS A DICTIONARY WITH THE COUNT OF EACH ITEM
    duplicates = {}
    filtered_list = []
    for item in list:
        if item != "Joker":
            value = item.split("-")[0]  # Get the value part of the card
            filtered_list.append(item)
    for item in filtered_list:
        value = item.split("-")[0]  # Get the value part of the card
        if value in duplicates:
            duplicates[value] += 1
        else:
            duplicates[value] = 1
    return duplicates
    
def check_pair(duplicates_dict, jokers): #***COMPLETE in theory
    # Checks cards in a list to provide a boolean response to if the list contains a pair
    # TAKES A LIST
    # CHECKS THE NUMBER OF EACH ITEM
    # IF TWO ITEM VALUES ARE ==, RETURN TRUE
    # ELSE, RETURN FALSE
    for count in duplicates_dict.values():
        if count == 2:
            return True
    if jokers >= 1 and len(duplicates_dict) >= 1:
        return True
    if jokers >=2:
        return True
    return False

def check_twopair(duplicates_dict, jokers): #***COMPLETE in theory
    # Checks cards in a list to provide a boolean response to if the list contains two pairs
    # TAKES A DICT
    # CHECKS THE NUMBER OF EACH ITEM
    # IF TWO ITEM VALUES ARE ==, RETURN TRUE
    # ELSE, RETURN FALSE
    pair_count = 0
    singles_count = 0
    
    for count in duplicates_dict.values():
        if count == 2:
            pair_count += 1
        elif count == 1:
            singles_count += 1
    if pair_count >= 2:
        return True
    
    if pair_count == 1 and jokers >= 1 and singles_count >= 1:
        return True
    if pair_count == 0 and jokers >= 2 and singles_count >= 2:
        return True

    return False

def check_fourofakind(duplicates_list, jokers): #***COMPLETE in theory
    # Checks cards in a list to provide a boolean response to if the list contains a four-of-a-kind
    # TAKES A LIST
    # CHECKS THE value OF EACH ITEM
    # IF 4 ITEMS ARE THE SAME VALUE, RETURN TRUE
    # ELSE, RETURN FALSE
    for count in duplicates_list.values():
        if count == 4:
            return True
        if count == 3 and jokers >= 1:
            return True
        if count == 2 and jokers >= 2:
            return True
    
    return False

def check_threeofakind(duplicates_list, jokers): #***COMPLETE in theory
    # Checks cards in a list to provide a boolean response to if the list contains a three-of-a-kind
    # TAKES A LIST
    # CHECKS THE value OF EACH ITEM
    # IF 3 ITEMS ARE THE SAME VALUE, RETURN TRUE
    # ELSE, RETURN FALSE
    for count in duplicates_list.values():
        if count == 3:
            return True
        if count == 2 and jokers >= 1:
            return True
        if count == 1 and jokers >= 2:
            return True
    return False

def check_fiveofakind(duplicates_list, jokers): #***COMPLETE in theory
    # Checks cards in a list to provide a boolean response to if the list contains a five-of-a-kind
    # TAKES A LIST
    # CHECKS THE value OF EACH ITEM
    # IF 5 ITEMS ARE THE SAME VALUE, RETURN TRUE
    # ELSE, RETURN FALSE
    for count in duplicates_list.values():
        if count == 5:
            return True
        if count == 4 and jokers >= 1:
            return True
        if count == 3 and jokers >= 2:
            return True
    return False
    
def check_highcard(hand): #COMPLETE - Theoretically Joker-Proof. Added a fallback to alert if a Joker makes it to this stage
    # Checks cards in a list to provide the highest card value present
    # TAKES A LIST
    # CHECKS THE value OF EACH ITEM
    # STORE THE HIGHEST VALUE
    # RETURN HIGHEST VALUE ITEM
    try:
        highest_value = 0
        highest_index = 0
        for cards in hand:
            if cards == "Joker":
                raise ValueError
            divided_values = cards.split("-")
            if divided_values[0] == "A":
                highest_value = 14
                highest_index = hand.index(cards)
            elif divided_values[0] == "K":
                highest_value = 13
                highest_index = hand.index(cards)
            elif divided_values[0] == "Q":
                highest_value = 12
                highest_index = hand.index(cards)
            elif divided_values[0] == "J":
                highest_value = 11
                highest_index = hand.index(cards)
            elif int(divided_values[0]) > highest_value:
                highest_value = int(cards[0])
                highest_index = hand.index(cards)
        return highest_index, highest_value
    except ValueError:
        print("JOKER ERROR: check_highcard Reader broke because a joker made it past the other hand checks.")

def check_fullhouse(duplicates_dict, jokercount): # NEW FUNCTION full house check
    actual_ranks = list(duplicates_dict.keys())

    for i in range(len(actual_ranks)):
        rank1 = actual_ranks[i]
        count1 = duplicates_dict[rank1]

        jokers_needed_for_three = max(0, 3 - count1)

        if jokers_needed_for_three <= jokercount: #In the event that I ever add more jokers or wild capability
            remaining_jokers_after_three = jokercount - jokers_needed_for_three

            if remaining_jokers_after_three >= 2:
                return True

            for j in range(len(actual_ranks)):
                if i == j: # Skip the rank already used for three-of-a-kind
                    continue

                rank2 = actual_ranks[j]
                count2 = duplicates_dict[rank2]

                jokers_needed_for_pair = max(0, 2 - count2)

                if jokers_needed_for_pair <= remaining_jokers_after_three:
                    return True 

    return False

def hand_check(hand_list): #!!! INCOMPLETE !!! Needs testing to see if the new joker mechanics work
    # Run through the different hand check defined functions, ranked in order of most valuable.
    # Return most prominent hand type and value
    # Remember to create a statement for IF Flush AND Straight == True, Straight Flush
    # Also create something for Royal Flush
    joker_total = joker_counter(hand_list)
    duplicates_dict = duplicate_dict_counter(hand_list)
    # Results:
    pair = check_pair(duplicates_dict, joker_total)
    two_pair = check_twopair(duplicates_dict, joker_total)
    three_kind = check_threeofakind(duplicates_dict, joker_total)
    four_kind = check_fourofakind(duplicates_dict, joker_total)
    five_kind = check_fiveofakind(duplicates_dict, joker_total)
    straight = check_straight(hand_list, joker_total)
    flush = check_flush(hand_list)
    fullhouse = check_fullhouse(duplicates_dict, joker_total)

    if five_kind == "true":
        return "Five Of A Kind", 0
    elif straight == True and flush == True:
        return "Straight Flush", 1
    elif four_kind == True:
        return "Four Of A Kind" , 2
    elif fullhouse == True:
        return "Full House" , 3
    elif flush == True:
        return "Flush" , 4
    elif straight == True:
        return "Straight" , 5
    elif three_kind == True:
        return "Three Of A Kind" , 6
    elif two_pair == True:
        return "Two Pair" , 7
    elif pair == True:
        return "Pair" , 8
    else:
        return "High Card" , 9

def joker_counter(hand_list): #COMPLETE
    counter = 0
    for card in hand_list:
        if card == "Joker":
            counter += 1
    return counter

def win_message():
    print("|--------------|")
    print("|***You Win!***|")
    print("|--------------|")

def lose_message():
    print("|---------------|")
    print("|***You Lose!***|")
    print("|---------------|")

# CURRENT GAMES
def twenty_one(): #FINISHED
    while True:
        current_deck = DECKOFCARDS
        current_deck.remove("Joker")
        current_deck.remove("Joker")
        player_hand = deal_cards(current_deck, 2)
        dealer_hand = deal_cards(current_deck, 2)
        dealer_value = int(compute_card_value(dealer_hand))
        player_value = int(compute_card_value(player_hand))
        print(f"Your Hand: {player_hand}\nTotal Value: {player_value}")
        while True:
            value = hit_card(current_deck, player_hand)
            if value == False:
                break
            player_value = int(compute_card_value(player_hand))
            if player_value > 21:
                print("-----------------------")
                print("\nBust! You exceeded 21.\n")
                print("-----------------------")
                break
            elif player_value == 21:
                print("-----------------------")
                print("\nBlackjack! You hit 21.\n")
                print("-----------------------")
                break
            else:
                print(f"Your Hand: {player_hand}\nTotal Value: {player_value}")
                continue
        dealer_value = int(compute_card_value(dealer_hand))
        player_value = int(compute_card_value(player_hand))
        if ((21 - dealer_value) <= (21 - player_value)) or player_value > 21:
            print(f"\nDealer Wins!\nDealer Hand: {dealer_hand}\nDealer Value: {dealer_value}")
        else:
            print(f"\nYou Win!")
            print(f"\nDealer Hand: {dealer_hand}\nDealer Value: {dealer_value}")
        print("-----------------------")
        print(f"Your Final Hand: {player_hand}\nFinal Value: {player_value}")
        print("-----------------------")
        break

def basic_poker(): #Functional But Not Complete
    current_deck = DECKOFCARDS
    #DEAL CARDS TO PLAYER
    player_hand = deal_cards(current_deck, 5)
    player_jokers = joker_counter(player_hand)
    print(f"Your Hand: {player_hand}")
    #DEAL CARDS TO COMPUTER
    dealer_hand = deal_cards(current_deck, 5)
    dealer_jokers = joker_counter(dealer_hand)

    #CHECK IF USER WANTS TO DISCARD CARDS
    user_discard_yn = get_str("Would you like to discard any cards? (y/n) ", ["y","n","Y","N"])
    if user_discard_yn in ["y", "Y"]:
        discarded_total = discard_cards(player_hand)
        if discarded_total != "cancel":
            player_hand += deal_cards(current_deck, discarded_total)
        player_jokers = joker_counter(player_hand)
    
    print(f"End Player Hand: {player_hand}")
    hand_type = hand_check(player_hand)
    print(hand_type)

    dealer_hand_type = hand_check(dealer_hand)
    print(f"\nDEALER HAND: {dealer_hand}")
    print(dealer_hand_type)

    if dealer_hand_type[0] == "High Card" and hand_type[0] == "High Card":
        dealer_highcard, dealer_highvalue = check_highcard(dealer_hand)
        player_highcard, player_highvalue = check_highcard(player_hand)
        print(f"DEALER HIGHCARD: {dealer_hand[dealer_highcard]}")
        print(f"YOUR HIGHCARD: {player_hand[player_highcard]}")
        if dealer_highvalue >= player_highvalue:
            lose_message()
        else:
            win_message()
    elif dealer_hand_type[1] > hand_type[1]:
        win_message()
    else:
        lose_message()
    
# RUN CODE

if __name__ == "__main__":
    main()