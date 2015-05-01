""" Friday game.
"""

import collections

from tgif import component_factory, context, turn


Result = collections.namedtuple('Result', ['won', 'score'])
""" The result of a friday game.
"""


class Friday:
    """ A friday board game.
    """

    def __init__(self, level, agent):
        self._level = level
        self._context = None
        self._agent = agent
        self._won = False

    @property
    def life(self):
        """ Get life. """
        # TODO raise GameNotRunException
        return None if self._context is None else self._context.life

    @property
    def score(self):
        """ Get score. """
        # TODO raise GameNotRunException
        return None if self._context is None else self._context.score

    @property
    def piles(self):
        """ Get all piles. """
        # TODO raise GameNotRunException
        return None if self._context is None else self._context.piles

    def start(self):
        """ Run the game.
        """
        self._context = context.Context(component_factory.ByLevel(self._level))
        cur_turn = turn.Starting(self._context, self._agent)
        while not cur_turn.game_ended():
            cur_turn = cur_turn.next()
            cur_turn.perform()
        self._won = cur_turn.game_won()
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
