""" An agent does actions in a game.
"""
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

    def battle(self, visible, enemy):
        """ Generates battle actions.
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

    def battle(self, visible, enemy):
        while True:
            self._print("Select action (draw/use/end):")
            action = self._input()
            if action == "draw":
                self._print("Draw a card, not yet implemented.")
                yield None
            elif action == "use":
                idx = self.select_card(visible, visible.cards)
                visible.cards[idx].use()
                self._print("Use a card.")
            elif action == "end":
                self._print("End the battle.")
                self._print("life = {}".format(visible.life))
                break
            else:
                self._print("Invalid action \"{}\"".format(action))

def console():
    return File(sys.stdin, sys.stdout)
