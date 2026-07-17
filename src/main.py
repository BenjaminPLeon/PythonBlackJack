from game import Game


suits = ["H", "C", "D", "S"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

if __name__ == "__main__":
    name = input("Enter your name: ").strip() or "Player"
    game = Game(player_name=name, starting_chips=100, num_decks=1)
    game.play()