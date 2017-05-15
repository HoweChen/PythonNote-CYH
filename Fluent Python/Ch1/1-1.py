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

# print top 3 cards of the deck
print(deck[:3])
# iterable deck
for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

# keyword "in" is also available
print(Card('Q', 'hearts') in deck)  # True
print(Card('Q', 'fuck') in deck)  # False

# sort the deck according to its suit_value and its rank_value
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# use sorted with 'key' keyword to sort the whole tuple
# according to this key, in this case is the rank_value returned by
# spades_high funcion
sorted_deck = sorted(deck, key=spades_high)

for card in sorted_deck:
    print(card)

# The reason why choice(deck) would automatically worked on deck._cards is that
#  we re-write the __getitem__ method to get the return of self cards position
# so we use deck[position] would return the _cards, so that random.choice could
# be used on this sequence, which is deck._cards

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
