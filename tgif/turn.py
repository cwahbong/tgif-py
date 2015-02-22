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
            for action in agent.battle(context.visible_part, fight):
                action(context)
            if context.battle_field.won():
                context.own_pile.discard(fight)
            else:
                damage = context.battle_field.health_lose()
                context.adventure_pile.discard(fight)
                context.life -= damage
                agent.discard(context.controller, damage)
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
        return context.agent.select_one(context.visible_part, pirates)

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
        adventures = None # TODO take 2 adventures from context
        if len(adventures) == 1:
            if agent.optional(context.controller, adventures[0]):
                return adventures[0]
            else:
                return None
        else:
            idx = agent.select_one(context.controller, adventures)
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
