import game
suits = ["H", "C", "D", "S"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
player_input = True

current_game = game.Game(num_players=1, num_decks=4, dealer_stand=17, suits=suits, faces=faces)
current_game.initial_deal()
current_game.print_dealer_hand()
current_game.print_player_hand()
current_game.check_values(initial=True)
current_game.get_input()