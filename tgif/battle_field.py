""" All battle information in a turn.
"""

class BattleCard:
    """ Information for a card in battle field.
    """
    def __init__(self, card, free):
        self._card = card
        self._free = free
        self.used = False
        self.doubled = False
        self.destroyed = False

    def use(self, context):
        if not self.used:
            self.card.use(context)
            self.used = True

    @property
    def free(self):
        return self._free

    @property
    def fighting_value(self):
        if self.destroyed:
            return 0
        value = self._card.fighting_value
        if self.doubled:
            value *= 2
        return value


class BattleField:
    """ Battle information in a turn.
    """
    def __init__(self, enemy=None, step=0):
        self._enemy = enemy
        self._free_cards = []
        self._additional_cards = []
        self._additional_limit = 0
        self._step = step

    @property
    def free_limit(self):
        return self._enemy.free_cards_num()

    @property
    def additional_limit(self):
        return self._additional_limit

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        if value >= 0:
            self._step = value

    def new_battle(self, enemy=None):
        if self._enemy is not None:
            self._free_cards = []
            self._additional_cards = []
            self._additional_limit = 0
        self._enemy = enemy

    def add_free(self, card):
        if len(self._free_cards) >= self.free_limit:
            return False
        self._free_cards.append(BattleCard(card, True))
        return True

    def get_free(self):
        return list(self._free_cards)

    def add_additional(self, card):
        if len(self._additional_cards) >= self.additional_limit:
            return False
        self._additional_cards.append(card)
        return True

    def get_additional(self):
        return list(self._additional_cards)

    def add_additional_limit(self, num):
        self._additional_limit += num

    @property
    def fighting_value(self):
        free = sum(bc.fighting_value for bc in self._free_cards)
        additional = sum(bc.fighting_value for bc in self._additional_cards)
        # TODO deal with highest zero
        # TODO deal with pirate modifier.
        return free + additional

    def won(self):
        return self.health_lose() == 0

    def health_lose(self):
        return self.fighting_value - self._enemy.hazard_value
