""" A turn manager is a state machine that manages turn transition.
"""

from tgif import turn

class TurnManager:
    def __init__(self, context, agent):
        self._context = context
        self._agent = agent
        self._turn = turn.Starting(self._context, self._agent)

    def perform_turn(self):
        self._turn = self._turn.next()
        self._turn.perform()

    def game_ended(self):
        return self._turn.game_ended()

    def game_won(self):
        return self._turn.game_won()
