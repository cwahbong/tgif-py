""" Card data in this file.
"""

import itertools

from tgif import ability, card

def startings():
    """ All 18 starting cards.
    """
    return itertools.chain(
        (card.starting(2)) * 1,
        (card.starting(1)) * 3,
        (card.starting(0)) * 8,
        (card.starting(0, ability.Life(2))) * 1,
        (card.starting(-1)) * 5
    )

_adventures = {
    1: itertools.chain(
        (0, ability.BelowThePile()) * 1,
        (0, ability.Cards(2))       * 2,
        (0, ability.Copy())         * 1,
        (0, ability.Destroy())      * 1,
        (0, ability.Exchange(2))    * 1,
        (0, ability.Life(1))        * 1,
        (0, ability.Step())         * 1,
    ),
    2: itertools.chain(
    ),
    3: itertools.chain(
    ),
    4: itertools.chain(
    ),
    5: itertools.chain(
    ),
}
def adventures():
    """ All adventure cards.
    """
    for level, details in _adventures:
        for detail in details:
            yield card.adventure(detail[0], detail[1], level)

def normal_agings():
    """ All normal aging cards.
    """
    return itertools.chain(
        (card.aging(0, ability.HighestZero())) * 2,
        (card.aging(0, ability.NegLife(1)))   * 1,
        (card.aging(0, ability.Stop()))        * 1,
        (card.aging(-1))                       * 1,
        (card.aging(-2))                       * 2,
        (card.aging(-3))                       * 1,
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
    return ()
