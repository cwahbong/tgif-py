""" Action enums.
"""

import enum


class Action(enum.Enum):
    draw_free = 1
    draw_additional = 2
    use = 3
    destroy = 4
    end_draw = 5
    end_fight = 6


class _Drawing:
    def __init__(self, context):
        self._context = context

    def draw_additional(self):
        """ Draw an additional card.
        """
        def action():
            """ Inner. """
            card = self._context.piles.own.draw()
            self._context.battle_field.add_additional(card)
        return action

    def destroy(self, battle_card):
        def action():
            if battle_card.destroy:
                return
            if battle_card._card.destroy_value <= self._context.battle_field.destroyable:
                battle_card.destroy = True
                self._context.battle_field.destroyable -= battle_card._card.destroy_value
        return action


def use_effect(free, idx):
    def _action(context):
        if free:
            context.battle_field.free[idx].use()
        else:
            context.battle_field.additional[idx].use()
    return _action


def pay_life():
    def _action(context):
        context.life -= 1
        context.battle_field.add_additional_limit(1)
    return _action
