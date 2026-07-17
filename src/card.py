class Card:
    """Represents a single playing card."""

    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        """Base blackjack value of the card (Ace treated as 11 by default)."""
        if self.rank in ("Jack", "Queen", "King"):
            return 10
        if self.rank == "Ace":
            return 11
        return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return str(self)