""" Turn represents a minimum unit of flow in the game.
"""

class Base:
    """ A base turn.
    """

    def _get_fight(self, context, agent):
        """ Get a fight card by given context.
        """
        raise NotImplementedError()

    def _end(self, context, agent):
        """ Ends a turn.
        """
        raise NotImplementedError()

    def execute(self, context, agent):
        """ Execute a turn.
        """
        fight = self._get_fight(context, agent)
        if fight is not None:
            context.battle_field.new_battle(fight)
            for action in agent.battle(context, fight):
                action(context)
            if context.battle_field.won():
                context.own_pile.discard(fight)
            else:
                damage = context.battle_field.health_lose()
                context.adventure_pile.discard(fight)
                context.life -= damage
                agent.discard(context, damage)
        self._end(context, agent)

    def game_ended(self, context):
        """ Indicates that the game should be end.
        """
        raise NotImplementedError()


class Pirate(Base):
    """ A turn that encounters a pirate card.
    """
    def _get_fight(self, context, agent):
        pirates = None # TODO Take pirates from context
        return context.agent.select_one(context, pirates)

    def _end(self, context, agent):
        pass

    def game_ended(self, context):
        return len(context.pirate_pile) == 0


class Adventure(Base):
    """ A turn that encounters an adventure card.
    """
    def __init__(self):
        self._count = 0

    def _get_fight(self, context, agent):
        adventures = context.piles.adventure.multidraw(2)
        if len(adventures) == 1:
            if agent.optional_enemy(context, adventures[0]):
                return adventures[0]
            else:
                return None
        else:
            idx = None
            while idx is None:
                idx = agent.select_enemy(context, adventures)
            return adventures[idx]

    def _end(self, context, agent):
        if len(context.comp.adventure_pile) == 0:
            if self._count == 2:
                context.turn = Pirate()
            else:
                self._count += 1
            context.adventure_pile.prepare()

    def game_ended(self, context):
        return False
