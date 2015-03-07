""" Card data in this file.
"""

import itertools

from tgif import ability, card

def startings():
    """ All 18 starting cards.
    """
    return itertools.chain(
        [card.starting(2)]                  * 1,
        [card.starting(1)]                  * 3,
        [card.starting(0)]                  * 8,
        [card.starting(0, ability.life(2))] * 1,
        [card.starting(-1)]                 * 5,
        )

def adventures():
    """ All adventure cards.
    """
    return itertools.chain(
        # level 1
        [card.adventure(1, 0, ability.below_the_pile())] * 1,
        [card.adventure(1, 0, ability.cards(2))]         * 2,
        [card.adventure(1, 0, ability.copy())]           * 1,
        [card.adventure(1, 0, ability.destroy())]        * 1,
        [card.adventure(1, 0, ability.exchange(2))]      * 2,
        [card.adventure(1, 0, ability.life(1))]          * 2,
        [card.adventure(1, 0, ability.step())]           * 1,
        # level 2
        [card.adventure(2, 1, ability.below_the_pile())] * 1,
        [card.adventure(2, 1, ability.copy())]           * 1,
        [card.adventure(2, 1, ability.destroy())]        * 1,
        [card.adventure(2, 1, ability.double())]         * 1,
        [card.adventure(2, 1, ability.life(1))]          * 2,
        [card.adventure(2, 2, ability.null())]           * 2,
        # level 3
        [card.adventure(3, 2, ability.cards(1))]         * 1,
        [card.adventure(3, 2, ability.destroy())]        * 1,
        [card.adventure(3, 2, ability.double())]         * 1,
        [card.adventure(3, 2, ability.exchange(1))]      * 1,
        [card.adventure(3, 2, ability.life(1))]          * 1,
        [card.adventure(3, 2, ability.sort())]           * 1,
        # level 4
        [card.adventure(4, 3, ability.cards(1))]         * 1,
        [card.adventure(4, 3, ability.destroy())]        * 1,
        [card.adventure(4, 3, ability.exchange(1))]      * 1,
        [card.adventure(4, 3, ability.sort())]           * 1,
        # level 5
        [card.adventure(5, 4, ability.null())]           * 2,
        )

def normal_agings():
    """ All normal aging cards.
    """
    return itertools.chain(
        [card.aging(0, ability.highest_zero())] * 2,
        [card.aging(0, ability.neg_life(1))]    * 1,
        [card.aging(0, ability.stop())]         * 1,
        [card.aging(-1)]                        * 1,
        [card.aging(-2)]                        * 2,
        [card.aging(-3)]                        * 1,
        )

def difficult_agings():
    """ All 3 difficult aging cards.
    """
    return (
        card.aging(-4),
        card.aging(-5),
        card.aging(0, ability.neg_life(2)),
        )

def pirates():
    """ All pirate cards.
    """
    return ()
