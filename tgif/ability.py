""" Abilities, including both positive and negative.
"""

class Base:
    """ Base.
    """

    def __init__(self, effect, optional, stop_draw=False):
        self._effect = effect
        self._optional = optional
        self._used = False
        self._stop_draw = stop_draw

    @property
    def stop_draw(self):
        return self._stop_draw

    @property
    def effect(self):
        """ Effect function specified by the ability.
        """
        return self._effect

    @property
    def optional(self):
        """ Indicates that if the card effect is optional.
        """
        return self._optional

    @property
    def used(self):
        """ Indicated that if the card has been used in this battle.
        """
        return self._used

    def use(self, context):
        """ Use the card in battle.
        """
        if self._used:
            return False
        return self._effect(context)

def _null_effect(context):
    """ An effect that does nothing.
    """
    # pylint: disable=W0613


def null():
    """ Null ability.
    """
    return Base(_null_effect, False)


def below_the_pile():
    """ Put 1 card to the bottom of pile.
    """
    def _effect(context):
        """ See module docstring.
        """
        card = context.agent.select(context.visible, context.battle_field.cards)
        context.own_pile.put_below(card)

    return Base(_effect, True)


def cards(num):
    """ More free cards.
    """
    def _effect(context):
        """ See module docstring.
        """
        context.battle_field.free_card_num += num

    return Base(_effect, True)


def copy():
    """ Copy 1 ability.
    """
    def _effect(context):
        """ See module docstring.
        """
        card = context.agent.select(context.visible, context.turn.cards)
        card.effect(context)

    return Base(_effect, True)


def destroy():
    """ Destroy 1 card.
    """
    def _effect(context):
        """ See module docstring.
        """
        card = context.agent.select(context.visible, context.turn.cards)
        context.battle_field.destroy(card)

    return Base(_effect, True)


def double():
    """ Double fighting value of 1 card.
    """
    def _effect(context):
        """ See module docstring.
        """
        card = context.agent.select(context.visible, context.turn.cards)
        context.battle_field.double(card)

    return Base(_effect, True)


def exchange(num):
    """ Discard 1 card then draw 1 card.  Repeat n times.
    """
    def _effect(context):
        """ See module docstring.
        """
        for _ in num:
            card = context.agent.select(context.battle_field.cards)
            context.battle_field.exchange(card, context.own_pile.draw())

    return Base(_effect, True)


def life(num):
    """ Add n life(s).
    """
    def _effect(context):
        """ See module docstring.
        """
        context.life += num

    return Base(_effect, True)


def step():
    """ Step - 1
    """
    def _effect(context):
        """ See module docstring.
        """
        context.battle_field.step -= 1

    return Base(_effect, True)


def sort():
    """ Sort 3 cards / discard 1 of 3
    """
    def _effect(context):
        """ See module docstring.
        """
        sorted_cards = [context.own_pile.draw() for _ in range(3)]
        # TODO optional discard one card.
        # TODO put 2 ~ 3 cards back to the top of pile.

    return Base(_effect, True)


def highest_zero():
    """ Make highest fighing value to zero.  Cannot effect to same card again.
    """
    def _effect(context):
        """ See module docstring.
        """
        context.battle_field.highest_zero += 1

    return Base(_effect, False)


def neg_life(num):
    """ Lose life.
    """
    def _effect(context):
        """ See module docstring.
        """
        context.life -= num

    return Base(_effect, False)


def stop():
    """ Stop draw free card immediatly.
    """
    return Base(_null_effect, False, True)
