""" Abilities, including both positive and negative.
"""
import numbers

class Base:
    """ Base.
    """

    name = "base"
    """ The name of that card.
    """

    optional = True
    """ Indicates that if the card effect is optional.
    """

    stop_draw = False
    """ Indicates that if agent must stop draw free cards.
    """


    def prepare_battle_effect(self, context, agent):
        """ Effect specified by the ability.
        """

    def battle_effect(self, context, agent):
        """ Effect specified by the ability.
        """

    def after_battle_effect(self, context, agent):
        """ Effect specified by the ability.
        """


class PositiveIntegral(Base):
    """ Base class containing a positive integral num.
    """

    def __init__(self, num):
        if not isinstance(num, numbers.Integral):
            raise ValueError("num should be integral.")
        if num <= 0:
            raise ValueError("num should be positive.")
        self._num = num


class Null(Base):
    """ An ability that does nothing.
    """
    name = "none"
    optional = False


class BelowThePile(Base):
    """ Put 1 card to the bottom of pile.
    """
    name = "below the pile"

    def prepare_battle_effect(self, context, agent):
        card = agent.select(context.visible, context.battle_field.cards)
        context.own_pile.put_below(card)


class Cards(PositiveIntegral):
    """ Add num cards.
    """
    name = "Cards +{}"

    def __init__(self, num):
        super().__init__(num)
        self.name = Cards.name.format(num)

    def prepare_battle_effect(self, context, agent):
        context.battle_field.free_card_num += self._num


class Copy(Base):
    """ Copy 1 ability.
    """
    name = "copy"

    def prepare_battle_effect(self, context, agent):
        card = agent.select(context.visible, context.turn.cards)
        card.effect(context)


class Destroy(Base):
    """ Destroy 1 card.
    """
    name = "destroy"

    def prepare_battle_effect(self, context, agent):
        card = agent.select(context.visible, context.turn.cards)
        context.battle_field.destroy(card)


class Double(Base):
    """ Double fighting value of 1 card.
    """
    name = "double"

    def battle_effect(self, context, agent):
        card = agent.select(context.visible, context.turn.cards)
        context.battle_field.double(card)


class Exchange(PositiveIntegral):
    """ Discard 1 card then draw 1 card.  Repeat num times.
    """
    name = "exchange {}"

    def __init__(self, num):
        super().__init__(num)
        self.name = Exchange.name.format(num)

    def prepare_battle_effect(self, context, agent):
        for _ in self._num:
            card = agent.select(context.battle_field.cards)
            context.battle_field.exchange(card, context.own_pile.draw())


class Life(PositiveIntegral):
    """ Add num life.
    """
    name = "life +{}"

    def __init__(self, num):
        super().__init__(num)
        self.name = Life.name.format(num)

    def prepare_battle_effect(self, context, agent):
        context.life += self._num


class Step(Base):
    """ Step - 1
    """
    name = "step -1"

    def battle_effect(self, context, agent):
        context.battle_field.step -= 1


class Sort(Base):
    """ Sort 3 cards / discard 1 of 3
    """
    name = "sort"

    def prepare_battle_effect(self, context, agent):
        sorted_cards = [context.own_pile.draw() for _ in range(3)]
        # TODO optional discard one card.
        # TODO put 2 ~ 3 cards back to the top of pile.


class HighestZero(Base):
    """ Make highest fighing value to zero.  Cannot effect to same card again.
    """
    name = "highest = 0"
    optional = False

    def battle_effect(self, context, agent):
        context.battle_field.highest_zero += 1


class NegLife(PositiveIntegral):
    """ Lose life.
    """
    name = "life -{}"
    optional = False

    def __init__(self, num):
        super().__init__(num)
        self.name = NegLife.name.format(num)

    def after_battle_effect(self, context, agent):
        """ See module docstring.
        """
        context.life -= self._num


class Stop(Base):
    """ Stop draw free card immediatly.
    """
    name = "stop"
    stop_draw = True
