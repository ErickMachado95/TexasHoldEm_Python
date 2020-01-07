#class for card
import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def get_suit(self):
        return self.suit
    def get_value(self):
        return self.value


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Spade","Heart","Diamond","Club"]:
            for value in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                self.cards.append(Card(suit,value))

    def shuffle(self):
        for i in range(1000):
            x = random.randint(0,len(self.cards)-1)
            y = random.randint(0,len(self.cards)-1)
            temp = self.cards[x]
            self.cards[x] = self.cards[y]
            self.cards[y] = temp

    def draw(self):
        return self.cards.pop()

    def return_card(self,Card):
        self.cards.append(Card)

    def print_cards_in_deck(self):
        for cards in self.cards:
            print("Suit: ",cards.suit,"\nValue: ",cards.value)


