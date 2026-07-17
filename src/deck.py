from card import Card
import random

class Deck:
    """Represents a shuffled deck (or multiple decks) of cards."""

    def __init__(self, num_decks=1):
        self.cards = []
        self.num_decks = num_decks
        self.build()

    def build(self):
        self.cards = [
            Card(rank, suit)
            for _ in range(self.num_decks)
            for suit in Card.SUITS
            for rank in Card.RANKS
        ]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        """Deal a single card, reshuffling a fresh deck if empty."""
        if not self.cards:
            print("Deck empty — reshuffling a fresh deck...")
            self.build()
        return self.cards.pop()
