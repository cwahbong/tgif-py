""" An agent does actions in a game.
"""

class Base:
    """ Agent interface.
    """

    def optional(self, visible, enemy):
        """ Returns boolean
        """
        raise NotImplementedError()

    def select(self, visible, enemies):
        """ Returns index of selected enemy.
        """
        raise NotImplementedError()

    def battle(self, visible, enemy):
        """ Generates battle actions.
        """
        pass
