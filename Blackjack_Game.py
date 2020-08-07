# Aces = 1 or 11
# King, Queen and Jack = 10

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards) 
        
    def remove_one(self):
        
        return self.all_cards.pop(0)
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.all_cards:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp


class Player():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = False
    
    def add_cards(self, new_cards):
        self.cards.append(new_cards)
        self.value += values[new_cards.rank]
        if new_cards.rank == 'Ace' and self.value > 21:
            self.value -= 10


class Chips():
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
            
    def lose_bet(self):
        self.total -= self.bet   


def take_bets(chips):
    
        while True:
            try:
                chips.bet = int(input('Enter the amount you want to bet: '))
            except ValueError:
                print('Please enter an integer vaulue for the bet!')
            else:
                if chips.bet > chips.total:
                    print('Not sufficient funds available!')
                else:
                    break

def hit_or_stand(player, deck):
    
    global playing
    while True:
        x = input('Do you want to hit or stand? h or s : ')
        if x.lower() == 'h':
            player.add_cards(deck.remove_one())
        elif x.lower() == 's':
            print('Player Stands. Dealer is playing')
            playing = False
        else:
            print('Sorry, please try again!')
            continue
        break    


def show_some(player):
    total_cards = []
    for test in player.cards:
        total_cards.append(test)

    print("<card hidden>" + ' ')
    print(total_cards[1])
    
def show_all(player):
    total_cards = []
    for test in player.cards:
        total_cards.append(test)
        
    print(*total_cards)


while True:
    
    test_deck = Deck()
    test_deck.shuffle()
    
    player = Player()
    player.add_cards(test_deck.remove_one())
    player.add_cards(test_deck.remove_one())
    
    dealer = Player()
    dealer.add_cards(test_deck.remove_one())
    dealer.add_cards(test_deck.remove_one())
       
    player_chips = Chips()
    take_bets(player_chips)
    
    while playing:
        
        print('\nPlayer Cards: ')
        show_all(player)
        print('Player cards total value: ', player.value)
        print('\nDealer Cards: ')
        show_some(dealer)
        
        if player.value == 21:
            print('The winner is the player')
            player_chips.win_bet()
            print('Players total money is: ', player_chips.total)
            break
        elif player.value > 21:
            print('\nPlayer Cards: ')
            show_all(player)
            print('\nPlayer cards total value: ', player.value)    
            print('The winner is the dealer')
            player_chips.lose_bet()
            print('Players total money is: ', player_chips.total)
            break
        
        hit_or_stand(player, test_deck)
        
    
    if player.value < 21:
        while dealer.value < 17:
            dealer.add_cards(test_deck.remove_one())
            print('Adding to the dealers card list')
        
        print('\nDealer Cards:')
        show_all(dealer)
        print('Dealer cards total value: ', dealer.value)
            
        if dealer.value == 21:
            print('The winner is the Dealer!')
            player_chips.lose_bet()  
        elif dealer.value > 21:
            print('The winner is the Player!')
            player_chips.win_bet()
        elif player.value > dealer.value:
            print('The winner is the Player!')
            player_chips.win_bet()
            print(f'Players total money is {player_chips.total}')
        elif player.value < dealer.value:
            print('The winner is the Dealer!')
            player_chips.lose_bet()
            print(f'Players total money is {player_chips.total}')
        else:
            print('The game is a tie') 
            
    new_game = input('Do you want to play again? y or n: ')
    
    if new_game.lower() == 'y':
        playing = True
        continue
    else:
        print('The Game is Over!')
        break
