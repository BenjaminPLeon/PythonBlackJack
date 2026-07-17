from card import Card

class Deck:
    def __init__(self, suits, faces):
        self.cards = []
        for s in suits:
            for f in faces:
                self.cards.append(Card(s, f))
        # print("Deck made with " + str(len(suits)) + " suits and " + str(len(faces)) + " faces")
        