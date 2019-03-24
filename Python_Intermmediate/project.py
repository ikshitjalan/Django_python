from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():

    def __init__(self):
        print("Creating New Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling Cards")
        shuffle(self.allcards)

    def split_in_half(self):
        print("Spliting into two")
        return (self.allcards[:26],self.allcards[26:])

class Hand():

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Containing {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove(self):
        self.cards.pop()

class Player():

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))


        #INCOMPLETE
