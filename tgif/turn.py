""" Turn represents a minimum unit of flow in the game.
"""

class Turn:

    def _get_fight(self, context):
        raise NotImplementedError()

    def _end(self, context):
        raise NotImplementedError()

    def execute(self, context):
        """ Execute a turn.
        """
        fight = self._get_fight(context)
        if fight is not None:
            context.battle_field.new_battle(fight)
            for action in context.agent.battle(context.visible_part, fight):
                action(context)
            if context.battle_field.won():
                context.own_pile.discard(fight)
            else:
                damage = context.battle_field.health_lose()
                context.adventure_pile.discard(fight)
                context.life -= damage
                context.agent.discard(context.controller, damage)
        self._end()

    def game_ended(self, context):
        """ Indicates that the game should be end.
        """
        raise NotImplementedError()


class Pirate(Turn):
    def _get_fight(self, context):
        pirates = None # TODO Take pirates from context
        return context.agent.select_one(context.visible_part, pirates)

    def _end(self, context):
        pass

    def game_ended(self, context):
        return len(context.pirate_pile) == 0


class Adventure(Turn):
    def __init__(self):
        self._count = 0

    def _get_fight(self, context):
        adventures = None # TODO take 2 adventures from context
        if len(adventures) == 1:
            if context.agent.optional(context.controller, adventures[0]):
                return adventures[0]
            else:
                return None
        else:
            idx = context.agent.select_one(context.controller, adventures)
            return adventure[idx]

    def _end(self, context):
        if len(context.comp.adventure_pile) == 0:
            if self._count == 2:
                context.turn = Pirate()
            else:
                self._count += 1
            context.adventure_pile.prepare()

    def game_ended(self, context):
        return False
