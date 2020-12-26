from enum import Enum
from collections import namedtuple

INFINITY = float("infinity")

class Bounds:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

class Intervals(Enum):
    OPEN                     = '()'
    CLOSED                   = '[]'
    LEFT_OPEN = RIGHT_CLOSED = '(]'
    RIGHT_OPEN = LEFT_CLOSED = '[)'

    is_open                        = lambda interval: interval == Intervals.OPEN
    is_closed                      = lambda interval: interval == Intervals.CLOSED
    is_left_open = is_right_closed = lambda interval: interval == Intervals.LEFT_OPEN
    is_right_open = is_left_closed = lambda interval: interval == Intervals.LEFT_CLOSED

class Rules(Enum):
    Rule = namedtuple('Rule', ('prompt', 'bounds', 'interval'))

    HOUSE_COST           = Rule("Cost of house:        ", Bounds(1, INFINITY), Intervals.LEFT_CLOSED)
    DOWN_PAYMENT_PERCENT = Rule("Down payment percent: ", Bounds(0, 100),      Intervals.CLOSED)
    SAVINGS              = Rule("Saved:                ", Bounds(0, INFINITY), Intervals.LEFT_CLOSED)
    INTEREST_ON_SAVINGS  = Rule("Savings interest:     ", Bounds(0, 100),      Intervals.CLOSED)
    SALARY               = Rule("Salary:               ", Bounds(1, INFINITY), Intervals.LEFT_CLOSED)
    SALARY_PERCENT_SAVED = Rule("Salary saved percent: ", Bounds(0, 100),      Intervals.CLOSED)