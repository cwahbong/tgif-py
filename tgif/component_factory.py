""" Factory that helps initialize a context object.
"""

import random

from tgif import cards, life, pile


class Base:
    """ Base.
    """
    def life(self):
        """ Create initial life.
        """
        raise NotImplementedError()

    def max_life(self):
        raise NotImplementedError()

    def _pile_adventure(self):
        raise NotImplementedError()

    def _pile_aging(self):
        raise NotImplementedError()

    def _pile_own(self):
        raise NotImplementedError()

    def _pile_pirate(self):
        raise NotImplementedError()

    def piles(self):
        return pile.Piles(
            adventure=self._pile_adventure(),
            aging=self._pile_aging(),
            own=self._pile_own(),
            pirate=self._pile_pirate(),
        )


class Lite(Base):
    def life(self):
        return NotImplemented

    def piles(self):
        return NotImplemented


class ByLevel(Base):
    """ Initialize a context object by level.
    """
    def __init__(self, level):
        self._level = level

    def life(self):
        return 20 if self._level < 4 else 18

    def max_life(self):
        return self.life() + 2

    def _pile_adventure(self):
        return pile.shuffled(cards.adventures())

    def _pile_aging(self):
        difficult_agings = list(cards.difficult_agings())
        random.shuffle(difficult_agings)
        normal_agings = list(cards.normal_agings())
        if self._level < 3:
            normal_agings = normal_agings[:-1]
        random.shuffle(normal_agings)
        return pile.Pile(difficult_agings + normal_agings)

    def _pile_own(self):
        return pile.shuffled(cards.startings())

    def _pile_pirate(self):
        return pile.Pile(random.sample(cards.pirates(), 2))

    def piles(self):
        piles = super().piles()
        if self._level >= 2:
            piles.own.discard(piles.aging.draw())
            piles.own.shuffle()
        return piles
