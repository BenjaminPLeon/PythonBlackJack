from random import shuffle
from deck import Deck

class Game:
    def __init__(self, num_players, dealer_stand, num_decks, suits, faces, debug=False):
        self.debug = debug
        self.num_players = num_players
        self.dealer_stand = dealer_stand
        self.num_decks = num_decks
        self.suits = suits
        self.faces = faces
        self.master_deck = []
        self.player_hand = []
        self.dealer_hand = []
        for _ in range(self.num_decks):
            deck_builder = Deck(suits, faces)
            for c in deck_builder.cards:
                self.master_deck.append(c)
        shuffle(self.master_deck)
        self.game_over = False
        self.player_value = 0
            
    def initial_deal(self):
        # burn top card, then player gets 1, then dealer gets 1, then player gets second, then dealer gets second
        self.master_deck =  self.master_deck[1:]
        self.player_hand.append(self.master_deck.pop())
        self.dealer_hand.append(self.master_deck.pop())
        self.player_hand.append(self.master_deck.pop())
        self.dealer_hand.append(self.master_deck.pop())
        
    def print_dealer_hand(self, initial = True):
        if initial:
            print("dealer: " + str(self.dealer_hand[0].suit) + "/" + str(self.dealer_hand[0].face) + " | ?" )
        
    def print_player_hand(self):
        self.output = "Player: "
        for c in self.player_hand[:-1]:
            self.output += str(c.suit) + "/" + str(c.face) + " | "
        self.output += str(self.player_hand[-1].suit) + "/" + str(self.player_hand[-1].face)
        print(self.output)
        
    def check_values(self, initial=False):
        for c in self.player_hand:
            self.player_value += c.value
        if initial and self.player_value == 21:
            print("Blackjack!")
            self.game_over = True
        elif self.player_value > 21:
            
        # elif self.player_value > 21:
        #     for v in self.player_hand.value: # Using a list of cards currently
        #         if v == 11:
        #             self.player_value = self.player_value - 10
        #     if self.debug : print("Player value: " + str(self.player_value))
        # elif self.player_value > 21:
        #     print ("Bust!")
        #     self.game_over = True
        else:
            print("Player value: " + str(self.player_value))
            
    def get_input(self):
        if not self.game_over:
            answer = input("What do you wish to do? (Hit, Stand)")
            if answer == "H":
                self.hit()
            
    
    def hit(self):
        self.player_hand.append(self.master_deck.pop())
        self.print_player_hand()
        self.check_values()