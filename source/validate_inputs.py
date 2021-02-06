from enum import Enum
from collections import namedtuple

INFINITY = float("infinity")

def is_input_valid(value, rule):
    if can_convert_to_float(value):
        return is_range_valid(float(value), rule)
    else:
        return False

def can_convert_to_float(user_input):
    try:
        float(user_input)
    except ValueError:
        return False
    else:
        return True

def is_range_valid(value, rule):
    bounds = rule.value.bounds
    interval = rule.value.interval

    if Intervals.is_open(interval):       return bounds.lower < value < bounds.upper
    if Intervals.is_closed(interval):     return bounds.lower <= value <= bounds.upper
    if Intervals.is_left_open(interval):  return bounds.lower < value <= bounds.upper
    if Intervals.is_right_open(interval): return bounds.lower <= value < bounds.upper

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

_Rule = namedtuple('_Rule', ('prompt', 'bounds', 'interval', 'is_percent'))

class Rules(Enum):
    HOUSE_COST           = _Rule("Cost of house:        ", Bounds(1, INFINITY), Intervals.LEFT_CLOSED, is_percent=False)
    DOWN_PAYMENT_PERCENT = _Rule("Down payment percent: ", Bounds(0, 100),      Intervals.CLOSED,      is_percent=True)
    SAVINGS              = _Rule("Saved:                ", Bounds(0, INFINITY), Intervals.LEFT_CLOSED, is_percent=False)
    INTEREST_ON_SAVINGS  = _Rule("Savings interest:     ", Bounds(0, 100),      Intervals.CLOSED,      is_percent=True)
    SALARY               = _Rule("Salary:               ", Bounds(1, INFINITY), Intervals.LEFT_CLOSED, is_percent=False)
    SALARY_PERCENT_SAVED = _Rule("Salary saved percent: ", Bounds(0, 100),      Intervals.CLOSED,      is_percent=True)
