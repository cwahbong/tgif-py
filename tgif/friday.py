""" Friday game.
"""

import collections

from tgif import context, turn_manager


Result = collections.namedtuple('Result', ['won', 'score'])
""" The result of a friday game.
"""


class Friday:
    """ A friday board game.
    """

    def __init__(self, level, agent):
        self._context = context.Context(level)
        self._turn_manager = turn_manager.TurnManager(self._context, agent)
        self._won = False

    @property
    def life(self):
        """ Get life. """
        return self._context.life

    @property
    def score(self):
        """ Get score. """
        return self._context.score

    @property
    def piles(self):
        """ Get all piles. """
        return self._context.piles

    def start(self):
        """ Start the game.
        """
        while not self._turn_manager.game_ended():
            self._turn_manager.perform_turn()
        self._won = self._turn_manager.game_won()
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
