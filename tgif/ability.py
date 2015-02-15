""" Abilities, including both positive and negative.
"""

class Base:
    """ Base.
    """

    def __init__(self, effect, optional):
        self._optional = optional
        self._effect = effect

    def use(self, context):
        if self._optional:
            return False
        return self._effect(context)


def null():
    """ Null ability.
    """
    def _effect(context):
        # pylint: disable=W0613
        pass

    return Base(_effect, False)


def below_the_pile():
    """ Put 1 card to the bottom of pile.
    """
    def _effect(context):
        """ TODO below the pile effect
        """

    return Base(_effect, True)


def cards(num):
    """ More free cards.
    """
    def _effect(context):
        """ TODO cards effect
        """

    return Base(_effect, True)


def copy():
    """ Copy 1 ability.
    """
    def _effect(context):
        """ TODO copy effect
        """

    return Base(_effect, True)


def destroy():
    """ Destroy 1 card.
    """
    def _effect(context):
        """ TODO copy effect
        """

    return Base(_effect, True)


def double():
    """ Double fighting value of 1 card.
    """
    def _effect(context):
        """ TODO double effect
        """

    return Base(_effect, True)


def exchange(num):
    """ Discard 1 card then draw 1 card.  Repeat n times.
    """
    def _effect(context):
        """ TODO exchange effect
        """

    return Base(_effect, True)


def life(num):
    """ Add n life(s).
    """
    def _effect(context):
        """ TODO life effect
        """

    return Base(_effect, True)


def step():
    """ Step - 1
    """
    def _effect(context):
        """ TODO step effect
        """

    return Base(_effect, True)


def sort():
    """ Sort 3 cards / discard 1 of 3
    """
    def _effect(context):
        pass

    return Base(_effect, True)


def highest_zero():
    """ Make highest fighing value to zero.  Cannot effect to same card again.
    """
    def _effect(context):
        pass

    return Base(_effect, False)


def neg_life(num):
    """ Lose life at the end of fight.
    """
    def _effect(context):
        pass

    return Base(_effect, False)


def stop():
    """ Stop draw free card immediatly.
    """
    def _effect(context):
        pass

    return Base(_effect, False)
