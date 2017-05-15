import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    _cards = None

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# a new card
beer_card = Card('7', 'diamonds')
print(beer_card)

# a new deck
deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])

# pick a random card
print('Pick a random card')
randomCards = [choice(deck) for i in range(10)]
for itr, val in randomCards:
    print(itr + ' of ' + val)

# The reason why choice(deck) would automatically worked on deck._cards is that we re-write the 
# __getitem__ method so when we use random.choice() it calls the __getitem__ method so that it would
# return the self._cards member

# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#     _cards = None

#     def __init__(self):
#         self._cards = [Card(rank, suit)
#                        for suit in self.suits for rank in self.ranks]

#     def __len__(self):
#         return len(self._cards)


# deck = FrenchDeck()
# print(len(deck))  # 52
# # print(deck[0])  # not working
# print(deck._cards[0])  # worked
# print(deck._cards[-1])  # worked
# # print([choice(deck) for i in range(10)])  # not working
# print([choice(deck._cards) for i in range(10)])  # worked
