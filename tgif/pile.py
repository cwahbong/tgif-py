import random

class Pile:
    def __init__(self, cards):
        self._cards = list(cards)
        self._discards = []
        self.prepare()

    def prepare(self):
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
