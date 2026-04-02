class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        if face == "Ace":
            self.value = 11
        elif face in ["King", "Queen", "Jack"]:
            self.value = 10
        else:
            self.value = int(face)