""" Friday game.
"""

import collections

from tgif import battle_field, exception, pile, turn

class Context:
    """ The context of friday game.
    """
    def __init__(self, level, agent):
        # TODO prepare the aging pile
        # TODO prepare the own pile by level
        self._life = 0
        self.own_pile = pile.Pile([])
        self.adventure_pile = pile.Pile([])
        self.pirate_pile = pile.Pile([])
        self.turn = turn.Adventure()
        self.battle_field = battle_field.BattleField()
        self.agent = agent

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


Result = collections.namedtuple('Result', ['won', 'score'])
""" The result of a friday game.
"""


class Friday:
    """ A friday board game.
    """

    def __init__(self, level, agent):
        self._context = Context(level, agent)
        self._won = False

    def start(self):
        """ Start the game.
        """
        self._won = False
        try:
            while not self._context.turn.game_ended():
                self._context.turn.execute(self._context)
            self._won = True
        except exception.GameOver:
            pass
        return self.result

    @property
    def result(self):
        """ Get the result of the last run for this game.
        """
        return Result(self._won, self._context.score)


def start(level, agent):
    """ Shortcut to create, run, and get the result of a friday game.
    """
    return Friday(level, agent).start()
