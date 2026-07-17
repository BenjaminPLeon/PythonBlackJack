class Participant:
    """Base class for anyone holding a hand: player or dealer."""

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add_card(deck.deal())

    def reset(self):
        self.hand.clear()

    def show_hand(self, hide_first=False):
        if hide_first:
            hidden = "Hidden Card"
            visible = ", ".join(str(c) for c in self.hand.cards[1:])
            print(f"{self.name}'s hand: {hidden}, {visible}")
        else:
            print(f"{self.name}'s hand: {self.hand} (value: {self.hand.value})")

class Player(Participant):
    """A human player with chips they can bet."""

    def __init__(self, name, chips=100):
        super().__init__(name)
        self.chips = chips
        self.bet = 0

    def place_bet(self):
        while True:
            try:
                amount = int(input(f"{self.name}, you have {self.chips} chips. Enter your bet: "))
                if 0 < amount <= self.chips:
                    self.bet = amount
                    break
                print("Invalid bet amount. Try again.")
            except ValueError:
                print("Please enter a whole number.")

    def win_bet(self, multiplier=1):
        winnings = int(self.bet * multiplier)
        self.chips += winnings
        print(f"{self.name} wins {winnings} chips!")

    def lose_bet(self):
        self.chips -= self.bet
        print(f"{self.name} loses {self.bet} chips.")

    def push_bet(self):
        print(f"{self.name}'s bet is returned (push).")

class Dealer(Participant):
    """The dealer, which follows fixed hit/stand rules."""

    def __init__(self):
        super().__init__("Dealer")

    def should_hit(self):
        return self.hand.value < 17
            
class Hand:
    """Represents a hand of cards belonging to a player or dealer."""

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    @property
    def value(self):
        """Best blackjack value of the hand, adjusting Aces from 11 to 1 as needed."""
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "Ace")
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    @property
    def is_blackjack(self):
        return len(self.cards) == 2 and self.value == 21

    @property
    def is_bust(self):
        return self.value > 21

    def clear(self):
        self.cards = []

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)