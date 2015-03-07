"""
"""

import random

from tgif import cards


class Pile:
    def __init__(self, cards):
        self._cards = list(cards)
        self._discards = []

    def shuffle(self):
        """ Gather all cards in the pile and shuffle them.
        """
        self._cards += self._discards
        self._discards = []
        random.shuffle(self._cards)

    def draw(self):
        """ Draw a non-discarded card.
        """
        return self._cards.pop()

    def put_top(self, card):
        """ Put a card at the top of pile.
        """
        # TODO

    def put_bottom(self, card):
        """ Put a card at the bottom of the pile.
        """
        self._cards = [card] + self._cards


    def discard(self, card):
        """ Put a card to discarded.
        """
        self._discards.append(card)

    def discarded_cards(self):
        """ Show all discarded cards.
        """
        return self._discards

    @property
    def all_cards(self):
        """ Show all cards.
        """
        all_cards = self._cards + self._discards
        random.shuffle(all_cards)
        return all_cards


def shuffled(cards):
    new_cards = list(cards)
    random.shuffle(new_cards)
    return Pile(new_cards)


def aging(level):
    difficult_agings = list(cards.difficult_agings())
    random.shuffle(difficult_agings)
    normal_agings = list(cards.normal_agings())
    if level < 3:
        normal_agings = normal_agings[:-1]
    random.shuffle(normal_agings)
    return Pile(difficult_agings + normal_agings)


def own(level, aging_pile):
    startings = cards.startings()
    if level >= 2:
        startings.append(aging_pile.draw())
    return shuffled(startings)


def adventure():
    print(cards.adventures())
    return shuffled(cards.adventures())


def pirate():
    pirates = cards.pirates()
    assert len(pirates) >= 2
    random.shuffle(pirates)
    return Pile(pirates[:2])


class Piles:
    """ All card piles here.
    """
    def __init__(self, level):
        self.aging = aging(level)
        self.own = own(level, self.aging)
        self.adventure = adventure()
        self.pirate = pirate()
