""" Context holds all data that will be affected by the game flow and agent.
"""

from tgif import battle_field, component_factory


class Context:
    """ See module doc.
    """
    def __init__(self, comp_factory):
        self._life = comp_factory.life()
        self._max_life = comp_factory.max_life()
        self._piles = comp_factory.piles()
        self.battle_field = battle_field.BattleField()

    @property
    def life(self):
        """ Get current life.
        """
        return self._life

    @life.setter
    def life(self, value):
        """ Set current life.
        """
        self._life = min(value, self._max_life)

    @property
    def piles(self):
        """ Get all piles.
        """
        return self._piles

    @property
    def score(self):
        """ Score of a friday context.
        """
        def _own_score(card):
            """ Score of owned card.
            """
            return -5 if card.destroy_value == 2 else card.fighting_value
        life_score = self.life * 5
        own_pile_score = sum(_own_score(card) for card in self.piles.own.all_cards)
        pirate_score = len(self.piles.pirate.discarded_cards()) * 5
        return life_score + own_pile_score + pirate_score
