""" Turn represents a minimum unit of flow in the game.
"""

from tgif import action

class Base:
    """ A base turn.
    """
    def __init__(self, context, agent):
        self._context = context
        self._agent = agent

    def next(self):
        """ Do turn transition and return the next turn.
        """
        raise NotImplementedError()

    def perform(self):
        """ Action of a turn.
        """
        raise NotImplementedError()

    def game_ended(self):
        """ Indicates that the game is ended.
        """
        raise NotImplementedError()

    def game_won(self):
        """ Indicated that if the agent won the game.
        """
        return False


class Starting(Base):
    """All context should be initialized to this state."""
    def next(self):
        return Adventure(self._context, self._agent)

    def perform(self):
        assert False

    def game_ended(self):
        return False


class Ending(Base):
    """All context should be initialized to this state."""

    def next(self):
        assert False

    def perform(self):
        pass

    def game_ended(self):
        return True

    def game_won(self):
        return self._context.life >= 0


class Battle(Base):
    """A turn that contains a battle."""

    def _get_enemy(self):
        """ Get an enemy card by given context.
        """
        raise NotImplementedError()

    def _player_fighting(self, fight):
        for act, add_info in self._agent.battle_fighting(self._context, fight):
            self._context.operate(act, add_info)

    def _finish_fight(self, fight):
        if self._context.battle_field.won():
            self._context.piles.own.discard(fight)
        else:
            self._context.piles.adventure.discard(fight)
        damage = self._context.battle_field.health_lose()
        self._context.life -= damage

    def _player_destroying(self, fight):
        for act, add_info in self._agent.battle_destroying(self._context, fight):
            self._context.operate(act, add_info)

    def perform(self):
        """ Execute a turn.
        """
        enemy = self._get_enemy()
        if enemy is not None:
            self._context.battle_field.new_battle(enemy)

            self._player_fighting(enemy)
            self._finish_fight(enemy)
            self._agent.battle_result(
                self._context.battle_field.won(),
                self._context.life)
            self._player_destroying(enemy)

            # self._context.battle_field.cleanup()
            """
            for card in self._context.battle_field.get_free():
                if not card.destroyed:
                    self._context.piles.own.discard(card._card)
            for card in self._context.battle_field.get_additional():
                if not card.destroyed:
                    self._context.piles.own.discard(card._card)
            """

    def game_ended(self):
        return False


class Pirate(Battle):
    """ A turn that encounters a pirate card.
    """
    def _get_enemy(self):
        pirates = None # TODO Take pirates from context
        return self._agent.select_one(self._context, pirates)

    def next(self):
        if len(self._context.piles.pirate) == 0:
            return Ending(self._context, self._agent)


class Adventure(Battle):
    """ A turn that encounters an adventure card.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._count = 0

    def next(self):
        if len(self._context.piles.adventure) == 0:
            if self._count == 2:
                return Pirate(self._context, self._agent)
            else:
                self._count += 1
                self._context.piles.adventure.prepare()
        return self

    def _get_enemy(self):
        adventures = self._context.piles.adventure.multidraw(2)
        if len(adventures) == 1:
            if self._agent.optional_enemy(self._context, adventures[0]):
                return adventures[0]
            else:
                return None
        else:
            idx = None
            while idx is None:
                idx = self._agent.select_enemy(self._context, adventures)
            return adventures[idx]
