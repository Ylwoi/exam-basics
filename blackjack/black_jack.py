# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades

import random


class Card(object):
    def __init__(self):
        color_list = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        value_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.card = [str(random.choice(value_list)), str(random.choice(color_list))]


class Deck(object):
    def __init__(self, deck_number):
        self.deck_list = []
        self.count_cards = {'Clubs':0, 'Diamonds':0, 'Hearts':0, 'Spades':0}
        for card in range(int(deck_number)):
            self.deck_list.append(Card().card)
        for card_color in self.deck_list:
            if card_color[1] == self.count_cards[]



deck = Deck(12)
print(deck)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
top_card = deck.draw()
print(top_card)
print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades
