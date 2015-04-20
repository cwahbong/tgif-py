""" Abilities, including both positive and negative.
"""

class Base:
    """ Base.
    """

    def __init__(self, name_info, effect, optional, stop_draw=False):
        self._name_info = name_info
        self._effect = effect
        self._optional = optional
        self._stop_draw = stop_draw

    def effect(self, context, agent):
        """ Effect specified by the ability.
        """
        return self._effect(context, agent)

    @property
    def optional(self):
        """ Indicates that if the card effect is optional.
        """
        return self._optional

    @property
    def stop_draw(self):
        """ Indicates that if agent must stop draw free cards.
        """
        return self._stop_draw

    @property
    def name(self):
        return self._name_info


def _null_effect(context, agent):
    """ An effect that does nothing.
    """
    # pylint: disable=W0613


def null():
    """ Null ability.
    """
    return Base("none", _null_effect, False)


def below_the_pile():
    """ Put 1 card to the bottom of pile.
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        card = agent.select(context.visible, context.battle_field.cards)
        context.own_pile.put_below(card)

    return Base("below the pile", _effect, True)


def cards(num):
    """ More free cards.
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        context.battle_field.free_card_num += num

    return Base("cards", _effect, True)


def copy():
    """ Copy 1 ability.
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        card = agent.select(context.visible, context.turn.cards)
        card.effect(context)

    return Base("copy", _effect, True)


def destroy():
    """ Destroy 1 card.
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        card = agent.select(context.visible, context.turn.cards)
        context.battle_field.destroy(card)

    return Base("destroy", _effect, True)


def double():
    """ Double fighting value of 1 card.
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        card = agent.select(context.visible, context.turn.cards)
        context.battle_field.double(card)

    return Base("double", _effect, True)


class Exchange(Base):
    def __init__(self, num):
        super().__init__("Exchange {}", None, True)
        self._num = num

    def effect(self, context, agent):
        for _ in self._num:
            card = agent.select(context.battle_field.cards)
            context.battle_field.exchange(card, context.own_pile.draw())

    @property
    def name(self):
        return self._name_info.format(self._num)


exchange = Exchange


#def exchange(num):
#    """ Discard 1 card then draw 1 card.  Repeat n times.
#    """
#    def _effect(context, agent):
#        """ See module docstring.
#        """
#        for _ in num:
#            card = agent.select(context.battle_field.cards)
#            context.battle_field.exchange(card, context.own_pile.draw())
#
#    return Base("exchange", _effect, True)


class Life(Base):
    def __init__(self, num):
        super().__init__("life +{}", None, True)
        self._num = num

    def effect(self, context, agent):
        context.life += self._num

    @property
    def name(self):
        return self._name_info.format(self._num)


life = Life


def step():
    """ Step - 1
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        context.battle_field.step -= 1

    return Base("step - 1", _effect, True)


def sort():
    """ Sort 3 cards / discard 1 of 3
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        sorted_cards = [context.own_pile.draw() for _ in range(3)]
        # TODO optional discard one card.
        # TODO put 2 ~ 3 cards back to the top of pile.

    return Base("sort", _effect, True)


def highest_zero():
    """ Make highest fighing value to zero.  Cannot effect to same card again.
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        context.battle_field.highest_zero += 1

    return Base("highest = 0", _effect, False)


def neg_life(num):
    """ Lose life.
    """
    def _effect(context, agent):
        """ See module docstring.
        """
        context.life -= num

    return Base("life -", _effect, False)


def stop():
    """ Stop draw free card immediatly.
    """
    return Base("stop", _null_effect, False, True)
