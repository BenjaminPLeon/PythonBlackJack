from player import Player, Dealer
from deck import Deck


class Game:
    """Orchestrates a full game session across multiple rounds."""

    def __init__(self, player_name="Player", starting_chips=100, num_decks=1):
        self.deck = Deck(num_decks=num_decks)
        self.player = Player(player_name, chips=starting_chips)
        self.dealer = Dealer()

    def play(self):
        print("Welcome to Blackjack!\n")
        while self.player.chips > 0:
            self.play_round()
            if self.player.chips <= 0:
                print("You're out of chips! Game over.")
                break
            if not self._play_again():
                break
        print(f"\nThanks for playing, {self.player.name}! Final chips: {self.player.chips}")

    def play_round(self):
        self.player.reset()
        self.dealer.reset()
        self.player.place_bet()

        # Initial deal
        for _ in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)

        print()
        self.player.show_hand()
        self.dealer.show_hand(hide_first=True)

        # Check for immediate blackjacks
        if self.player.hand.is_blackjack or self.dealer.hand.is_blackjack:
            self._resolve_blackjacks()
            return

        self._player_turn()

        if self.player.hand.is_bust:
            print(f"\n{self.player.name} busts!")
            self.player.lose_bet()
            return

        self._dealer_turn()
        self._determine_winner()

    def _player_turn(self):
        while True:
            choice = input("\nDo you want to (h)it or (s)tand? ").strip().lower()
            if choice == "h":
                self.player.hit(self.deck)
                self.player.show_hand()
                if self.player.hand.is_bust:
                    return
            elif choice == "s":
                return
            else:
                print("Please enter 'h' or 's'.")

    def _dealer_turn(self):
        print()
        self.dealer.show_hand()
        while self.dealer.should_hit():
            print("Dealer hits.")
            self.dealer.hit(self.deck)
            self.dealer.show_hand()
        if self.dealer.hand.is_bust:
            print("Dealer busts!")

    def _resolve_blackjacks(self):
        player_bj = self.player.hand.is_blackjack
        dealer_bj = self.dealer.hand.is_blackjack
        self.dealer.show_hand()

        if player_bj and dealer_bj:
            print("\nBoth have Blackjack — it's a push!")
            self.player.push_bet()
        elif player_bj:
            print(f"\n{self.player.name} has Blackjack! Pays 3:2.")
            self.player.win_bet(multiplier=1.5)
        else:
            print("\nDealer has Blackjack. You lose.")
            self.player.lose_bet()

    def _determine_winner(self):
        player_value = self.player.hand.value
        dealer_value = self.dealer.hand.value

        print(f"\n{self.player.name}: {player_value} | Dealer: {dealer_value}")

        if self.dealer.hand.is_bust or player_value > dealer_value:
            self.player.win_bet()
        elif player_value < dealer_value:
            self.player.lose_bet()
        else:
            print("It's a push!")
            self.player.push_bet()

    def _play_again(self):
        choice = input("\nPlay another round? (y/n): ").strip().lower()
        return choice == "y"


if __name__ == "__main__":
    name = input("Enter your name: ").strip() or "Player"
    game = Game(player_name=name, starting_chips=100, num_decks=1)
    game.play()