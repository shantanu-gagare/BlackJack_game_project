import random

cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while input("Dou want to play BlackJack21? press y for playing any other key to quit ") == "y":
    our_players_cards = []
    computers_card = []

    for ran_cards_for_player in range(1, 3):
        random_cards = random.choice(cards_deck)
        our_players_cards.append(random_cards)
    for ran_cards_for_computer in range(1, 3):
        random_cards = random.choice(cards_deck)
        computers_card.append(random_cards)
    print(our_players_cards, f"total of your cards is {our_players_cards[0] + our_players_cards[1]}",
          f" Dealers card{computers_card[0]}")

    while sum(our_players_cards) < 21 and input(" 'Hit' or 'Stand', for hit press 'y' and for stand press 'n' ") == "y":
        random_cards = random.choice(cards_deck)
        our_players_cards.append(random_cards)
        sum_of_player = sum(our_players_cards)
        print(our_players_cards, sum_of_player, f" Dealers card {computers_card[0]}")

    if sum(our_players_cards) > 21 and 11 in our_players_cards:

        our_players_cards.remove(11)
        our_players_cards.append(1)
        while sum(our_players_cards) < 21 and input(
                " 'Hit' or 'Stand', for hit press 'y' and for stand press 'n' ") == "y":
            random_cards = random.choice(cards_deck)
            if random_cards == 11:
                our_players_cards.append(1)
                break
            our_players_cards.append(random_cards)
            sum_of_player = sum(our_players_cards)
            print(our_players_cards, sum_of_player, f" Dealers card {computers_card[0]}")
    elif sum(our_players_cards) > 21:
        print(
            f" Player Busted!!! Dealer had {computers_card} =  {sum(computers_card)}, & You had {our_players_cards} ="
            f" {sum(our_players_cards)} ")
        # break
    elif sum(computers_card) < 17:
        computers_card.append(random.choice(cards_deck))
    if sum(computers_card) > 21:
        print(
            f"Dealer Busted !!!!!  Dealer had {computers_card} = {sum(computers_card)}, & You had {our_players_cards} ="
            f" {sum(our_players_cards)}")
        # break
    elif sum(our_players_cards) > 21:
        print(f"Player Busted!!! Dealer had {computers_card} =  {sum(computers_card)}, & You had {our_players_cards} ="
            f" {sum(our_players_cards)}")
    elif sum(computers_card) > sum(our_players_cards):
        print(
            f"You Lost,  Dealer had {computers_card} =  {sum(computers_card)}, & You had {our_players_cards} ="
            f" {sum(our_players_cards)} ")
        # break

    elif sum(our_players_cards) > sum(computers_card):
        print(
            f"You Won,  Dealer had {computers_card} =  {sum(computers_card)}, & You had {our_players_cards} ="
            f" {sum(our_players_cards)} ")
        # break
    elif sum(our_players_cards) == sum(computers_card):
        print(
            f"Draw, Dealer had {computers_card} =  {sum(computers_card)}, & You had {our_players_cards} ="
            f" {sum(our_players_cards)} ")
        # break
