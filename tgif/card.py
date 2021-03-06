""" Card classes and functions go here.
"""

from tgif import ability

class Knowledge:
    def __init__(self, fighting_value, destroy_value, fighting_ability=ability.Null()):
        self._fighting_value = fighting_value
        self._destroy_value = destroy_value
        self._ability = fighting_ability

    @property
    def fighting_value(self):
        """ Accumulate fighting value to defeat the hazard.
        """
        return self._fighting_value

    @property
    def destroy_value(self):
        """ The sum of destroy value of destroyed cards can not exceed losing
        health this round.
        """
        return self._destroy_value

    def use_special(self):
        """ Optional special ability used during fighting.
        """
        pass

    def end_special_must(self):
        """ Required speical ability used at the end of fight.
        """
        pass


class Hazard:

    def __init__(self, free_cards_num, hazard_values, hazard_ability=ability.Null()):
        self._free_cards_num = free_cards_num
        self._hazard_values = tuple(hazard_values)
        assert len(self._hazard_values) == 3

    @property
    def free_cards_num(self):
        """ Number of free cards.
        """
        return self._free_cards_num

    def hazard_value(self, step):
        """ The goal of accumulated fighting value.
        """
        return self._hazard_values[step]


class FightingCard:

    def __init__(self, knowledge_card, hazard_card=None):
        self._knowledge = knowledge_card
        self._hazard = hazard_card

    @property
    def fighting_value(self):
        return self._knowledge.fighting_value

    @property
    def destroy_value(self):
        return self._knowledge.destroy_value

    # TODO other functions in knowledge

    # TODO other functions in hazard

    def hazard_value(self, step):
        return self._hazard.hazard_value(step)

    def __str__(self):
        return "FightingCard F<{}> D<{}> A<{}>".format(
            self.fighting_value,
            self.destroy_value,
            self._knowledge._ability.name)


def starting(fighting_value, fighting_ability=ability.Null()):
    return FightingCard(Knowledge(fighting_value, 1, fighting_ability))


def aging(fighting_value, fighting_ability=ability.Null()):
    return FightingCard(Knowledge(fighting_value, 2, fighting_ability))


_hazards = (
    None,
    Hazard(1, (0, 1, 3)),
    Hazard(2, (1, 3, 6)),
    Hazard(3, (2, 5, 8)),
    Hazard(4, (4, 7, 11)),
    Hazard(5, (5, 9, 14)),
)
def hazard(level):
    return _hazards[level]


def adventure(hazard_level, fighting_value, knowledge_ability):
    return FightingCard(Knowledge(fighting_value, 1, knowledge_ability),
            hazard(hazard_level))


class Pirate:

    def __init__(self, free_cards_num, hazard_value, pirate_ability=None):
        self._free_cards_num = free_cards_num
        self._hazard_value = hazard_value
        self._ability = pirate_ability
        # TODO special ability of pirate
