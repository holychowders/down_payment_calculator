from rules import Rules, Intervals
class Inputs:
    def collect_inputs(self):
        self.house_cost = collect_input(Rules.HOUSE_COST)
        self.down_payment_percent = collect_input(Rules.DOWN_PAYMENT_PERCENT)
        self.savings = collect_input(Rules.SAVINGS)
        self.interest_on_savings = collect_input(Rules.INTEREST_ON_SAVINGS)
        self.salary = collect_input(Rules.SALARY)
        self.salary_percent_saved = collect_input(Rules.SALARY_PERCENT_SAVED)

def collect_input(rule):
    value = input(rule.value.prompt)

    if is_input_valid(value, rule):
        return float(value)
    else:
        print("Invalid input")
        return collect_input(rule)

def  is_input_valid(value, rule):
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
