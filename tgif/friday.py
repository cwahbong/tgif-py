""" Friday game.
"""

import collections

from tgif import context, exception


Result = collections.namedtuple('Result', ['won', 'score'])
""" The result of a friday game.
"""


class Friday:
    """ A friday board game.
    """

    def __init__(self, level, agent):
        self._context = context.Context(level)
        self._agent = agent
        self._won = False

    def start(self):
        """ Start the game.
        """
        self._won = False
        try:
            while not self._context.turn.game_ended(self._context):
                self._context.turn.execute(self._context, self._agent)
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
