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
        [card.starting(0, ability.Life(2))] * 1,
        [card.starting(-1)]                 * 5,
        )

def adventures():
    """ All adventure cards.
    """
    return itertools.chain(
        # level 1
        [card.adventure(1, 0, ability.BelowThePile())]   * 1,
        [card.adventure(1, 0, ability.Cards(2))]         * 2,
        [card.adventure(1, 0, ability.Copy())]           * 1,
        [card.adventure(1, 0, ability.Destroy())]        * 1,
        [card.adventure(1, 0, ability.Exchange(2))]      * 2,
        [card.adventure(1, 0, ability.Life(1))]          * 2,
        [card.adventure(1, 0, ability.Step())]           * 1,
        # level 2
        [card.adventure(2, 1, ability.BelowThePile())]   * 1,
        [card.adventure(2, 1, ability.Copy())]           * 1,
        [card.adventure(2, 1, ability.Destroy())]        * 1,
        [card.adventure(2, 1, ability.Double())]         * 1,
        [card.adventure(2, 1, ability.Life(1))]          * 2,
        [card.adventure(2, 2, ability.Null())]           * 2,
        # level 3
        [card.adventure(3, 2, ability.Cards(1))]         * 1,
        [card.adventure(3, 2, ability.Destroy())]        * 1,
        [card.adventure(3, 2, ability.Double())]         * 1,
        [card.adventure(3, 2, ability.Exchange(1))]      * 1,
        [card.adventure(3, 2, ability.Life(1))]          * 1,
        [card.adventure(3, 2, ability.Sort())]           * 1,
        # level 4
        [card.adventure(4, 3, ability.Cards(1))]         * 1,
        [card.adventure(4, 3, ability.Destroy())]        * 1,
        [card.adventure(4, 3, ability.Exchange(1))]      * 1,
        [card.adventure(4, 3, ability.Sort())]           * 1,
        # level 5
        [card.adventure(5, 4, ability.Null())]           * 2,
        )

def normal_agings():
    """ All normal aging cards.
    """
    return itertools.chain(
        [card.aging(0, ability.HighestZero())]  * 2,
        [card.aging(0, ability.NegLife(1))]     * 1,
        [card.aging(0, ability.Stop())]         * 1,
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
        card.aging(0, ability.NegLife(2)),
        )

def pirates():
    """ All pirate cards.
    """
    return (
        # card.pirate(5, *, aging * 2),
        # card.pirate(*, *, all unresolved adventures),
        # card.pirate(7, 16, additional fight = 2 life),
        card.Pirate(6, 20),
        # card.pirate(9, 22, half fightings cards counted),
        card.Pirate(7, 25),
        card.Pirate(8, 30),
        card.Pirate(9, 35),
        card.Pirate(10, 40),
        # card.pirate(10, 52, fighting value += num of fighting cards),
        )
