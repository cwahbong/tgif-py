class BattleField:
    def __init__(self, enemy=None):
        self._enemy = enemy
        self._free_cards = []
        self._additional_cards = []
        self._additional_limit = 0

    @property
    def free_limit(self):
        return self._enemy.free_cards_num()

    @property
    def additional_limit(self):
        return self._additional_limit

    def new_battle(self, enemy=None):
        if self._enemy is not None:
            self._free_cards = []
            self._additional_cards = []
            self._additional_limit = 0
        self._enemy = enemy

    def add_free(self, card):
        if len(self._free_cards) >= self.free_limit:
            return False
        self._free_cards.append(card)
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

    def won(self):
        return self.health_lose() == 0

    def health_lose(self):
        # TODO
        pass
