""" Abilities, including both positive and negative.
"""

class Ability:
    """ Base.
        TODO
    """

    def use_once(self, context):
        pass

    def end_of_fight(self, context):
        pass

class BelowThePile(Ability):
    """ Put 1 card to the bottom of pile.
    """

class Cards(Ability):
    """ More free cards.
    """

class Copy(Ability):
    """ Copy 1 ability.
    """

class Destroy(Ability):
    """ Destroy 1 card.
    """

class Double(Ability):
    """ Double fighting value of 1 card.
    """

class Exchange(Ability):
    pass

class Life(Ability):
    """ Add life(s).
    """

class Step(Ability):
    pass

class Sort(Ability):
    pass


class HighestZero(Ability):
    """ Make highest fighing value to zero.  Cannot effect to same card again.
    """

class NegLife(Ability):
    """ Lose life at the end of fight.
    """

class Stop(Ability):
    """ Stop draw free card immediatly.
    """
