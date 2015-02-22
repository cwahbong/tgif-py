""" Context holds all data that will be affected by the game flow and agent.
"""

from tgif import battle_field, exception, pile, turn

class Context:
    """ See module doc.
    """
    def __init__(self, level):
        # TODO prepare the aging pile
        # TODO prepare the own pile by level
        self._life = 0
        self.own_pile = pile.Pile([])
        self.adventure_pile = pile.Pile([])
        self.pirate_pile = pile.Pile([])
        self.turn = turn.Adventure()
        self.battle_field = battle_field.BattleField()

    @property
    def life(self):
        """ Get current life.
        """
        return self._life

    @life.setter
    def life(self, value):
        """ Set current life, to maximum of 22.  Raise tgif.exception.GameOver
        if the life is negative.
        """
        self._life = value
        if self._life > 22:
            self._life = 22
        elif self._life < 0:
            raise exception.GameOver()

    @property
    def score(self):
        """ Score of a friday context.
        """
        def _own_score(card):
            """ Score of owned card.
            """
            return -5 if card.destroy_value == 2 else card.fighting_value
        life_score = self.life * 5
        own_pile_score = sum(_own_score(card) for card in self.own_pile.all_cards())
        pirate_score = len(self.pirate_pile.discarded_cards()) * 5
        return life_score + own_pile_score + pirate_score

