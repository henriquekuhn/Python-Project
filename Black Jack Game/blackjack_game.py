import random
from blackjack_art import logo

deck = {
        "espadas": [1,2,3,4,5,6,7,8,9,10,11,12], 
        "paus": [1,2,3,4,5,6,7,8,9,10,11,12], 
        "copas": [1,2,3,4,5,6,7,8,9,10,11,12],
        "ouro": [1,2,3,4,5,6,7,8,9,10,11,12]
        }
your_hand = {}
machine_hand = {}
decks_qty = []


def create_deck(decks):

    for _ in range(decks):
        decks_qty.append(deck)

def get_card(quantity, player):
    lista_your = []
    lista_machine = []
    for _ in range(quantity):
        random_deck = random.randint(0,(len(decks_qty)-1)) #Get a random deck
        random_nipe = random.choice(list(deck)) #Get a random nipe from the deck

        #Get a random card from 'random_deck' and 'random_nipe'
        #considering their actual size
        random_card = random.randint(1,len(decks_qty[random_deck][random_nipe]))

        #Remove the card from the deck to prevent it from being drawn again.    
        decks_qty[random_deck][random_nipe].pop(random_card-1)

        if player == 1: 
            if your_hand.get(random_nipe) is None:
                your_hand[random_nipe] = []         
            your_hand[random_nipe].append(random_card) #Create a dict with player cards
            
        else:
            if machine_hand.get(random_nipe) is None:
                machine_hand[random_nipe] = []         
            machine_hand[random_nipe].append(random_card) #Create a dict with dealer cards
            
    
def sum_points(hand):

    sum = 0
    for lst in hand.values():
        for n in lst:
            if n == 1:
                sum += 11
            elif n > 10:
                sum += 10
            else:
                sum += n 

        number_of_ones = count_ones_in_dict(hand)

        if number_of_ones > 0 and sum > 21:
            n = 0
            while n < number_of_ones and sum > 21:
                sum -= 10
                n+=1
    return sum


def count_ones_in_dict(hand):
    count_of_ones = sum(sublist.count(1) for sublist in hand.values() if isinstance(sublist, list))
    return count_of_ones

keep_playing = True
while keep_playing:
    print(logo)
    
    decks = int(input("Choose the number of decks: "))
    create_deck(decks)
    get_card(2, 1)
    print(f'\n- Your initial hand: {your_hand}')
    get_card(2, 2)
    print(f'- Machine initial hand: {random.choice(list(machine_hand))} {machine_hand[random.choice(list(machine_hand))][0]}')
    buy = input("\nDo you want to buy a card (y or n)? ")
    if buy == 'y':
        get_card(1, 1)
        print(f'\nYour new hand: {your_hand}')
    
    #   sum_points()    
    your_sum = sum_points(your_hand)
    machine_sum = sum_points(machine_hand)
    
    while machine_sum < 17:    
        get_card(1, 2)
        machine_sum = sum_points(machine_hand)
    
    print(f'\nTour Hand sum: {your_sum}')
    print(f'Dealer Hand sum: {machine_sum}')
    
    if your_sum > machine_sum:
        print(f"\nIt is a draw: {your_sum} points against {machine_sum} machine points!")
    elif your_sum > machine_sum and your_sum <= 21:
        print(f"\nYou Win with a sum of: {your_sum} points against {machine_sum} machine points!")
    elif your_sum > 21:
        print(f"\nTotal of {your_sum}, greater than 21. You lost!")
    else:
        print(f"\nMachine Wins with {machine_sum} against {your_sum}!")

    if input("\nWould you like to keep playing (y or n): ") == 'n':
        keep_playing = False

   

