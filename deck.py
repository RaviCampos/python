from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        cards = []
        for value in Deck.values:
            for suit in Deck.suits:
                cards.append(Card(value, suit))
        self.cards = cards

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        if num >= 52:
            num = 52
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        dealt = self.cards[-num::]
        self.cards = self.cards[:-num:]
        return dealt

    def count(self):
        return len(self.cards)
    
    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num = 1):
        return self._deal(num)


we = Card("2", "Hearts")

deck = Deck()
print(deck)
deck.shuffle()
print(deck.deal_hand())
print(deck)
