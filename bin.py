'''
This is a bin class for the roulette. It is simply the 38 bins where each bin
is a collection of the possible outcomes that are associated with each bin. The
outcomes reflect the winning bets that are paid for a particular bin on a roulette
wheel. We will represent each bin as a frozenset that holds the outcomes.
'''
from outcome import Outcome

class Bin():

    def __init__(self, * outcomes):
        self.outcomes = frozenset(outcomes)
    
    def add(self, outcome):
        if isinstance(outcome,Outcome):
            self.outcomes |= set([outcome])
        else:
            return

    def __str__(self):
        return ', '.join(map(str,self.outcomes))
