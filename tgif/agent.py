""" An agent does actions in a game.
"""
from tgif import action

import sys


class Base:
    """ Agent interface.
    """

    def optional_enemy(self, visible, enemy):
        """ Returns boolean
        """
        raise NotImplementedError()

    def select_enemy(self, visible, enemies):
        """ Returns index of selected enemy.
        """
        raise NotImplementedError()

    def select_card(self, visible, cards):
        """ Returns index of selected card.
        """
        raise NotImplementedError()

    def battle_fighting(self, visible, enemy):
        """ Generates battle actions.
        """
        raise NotImplementedError()

    def battle_destroying(self, visible, enemy):
        """ Generates battle destroy actions.
        """
        raise NotImplementedError()


class File(Base):
    """ An agent by given input file and output file.
    """

    def __init__(self, in_file, out_file):
        super().__init__()
        self._i_file = in_file
        self._o_file = out_file

    def _input(self):
        """ Get trimmed input line.
        """
        line = self._i_file.readline()
        return line.strip() if line is not None else None

    def _print(self, string):
        """ Print string in a line.
        """
        self._o_file.write("{}\n".format(string))

    def _print_battle_stat(self, visible):
        self._print("--- Life = {} ---".format(visible.life))

        free_num = len(visible.battle_field.get_free())
        self._print("--- Free {}/{} ---".format(free_num, visible.battle_field.free_limit))
        for idx, card in enumerate(visible.battle_field.get_free(), 1):
            self._print("{}. {}".format(idx, card._card))

        add_num = len(visible.battle_field.get_additional())
        self._print("--- Additional {}/{} ---".format(add_num, visible.battle_field.additional_limit))
        for idx, card in enumerate(visible.battle_field.get_additional(), 1):
            self._print("{}. {}".format(idx, card._card))

    def optional_enemy(self, visible, enemy):
        self._print("Optional enemy [Y/N]:")
        # TODO Print enemy information.
        string = self._input()
        if string == "Y":
            return True
        elif string == "N":
            return False
        else:
            self._print("Not a valid option.")
            return None

    def _select(self, visible, items):
        """ Select an item.
        """
        # TODO Print item information.
        try:
            idx = int(self._input())
            items[idx]
            return idx
        except ValueError:
            self._print("Not a valid index.")
            return None
        except IndexError:
            self._print("Index out of range.")
            return None

    def select_enemy(self, visible, enemies):
        for idx, enemy in enumerate(enemies):
            self._print("[{}] {}".format(idx, enemy))
        self._print("Select enemy <index>:")
        return self._select(visible, enemies)

    def select_card(self, visible, cards):
        self._print("Select card <index>:")
        return self._select(visible, cards)

    def battle_fighting(self, visible, enemy):
        while True:
            self._print_battle_stat(visible)
            self._print("Select action (draw free/draw additional/use/end draw/end fight):")
            act = self._input()
            if act == "draw free":
                yield action.Action.draw_free, None
            elif act == "draw additional":
                yield action.Action.draw_additional, None
            elif act == "use":
                idx = self.select_card(visible, visible.cards)
                # visible.cards[idx].use()
                yield action.Action.use, idx
            elif act == "end draw":
                yield action.Action.end_draw, None
            elif act == "end fight":
                break
            else:
                self._print("Invalid action \"{}\"".format(act))

    def battle_destroying(self, visible, enemy):
        while True:
            self._print("Select action (destroy/end)")
            act = self._input()
            if act == "destroy":
                yield action.Action.destroy, None
            elif act == "end":
                break
            else:
                self._print("Invalid action \"{}\"".format(act))

    def battle_result(self, won, life):
        """ Called upon the battle is end.
        """
        if won:
            self._print("Battle won.")
        else:
            self._print("Battle lost.")
        self._print("Life = {}.".format(life))


def console():
    return File(sys.stdin, sys.stdout)
