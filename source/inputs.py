from rules import Rules, Intervals
class InputsFromPrompt:
    def collect(self):
        self.house_cost = self._collect(Rules.HOUSE_COST)
        self.down_payment_percent = self._collect(Rules.DOWN_PAYMENT_PERCENT)
        self.savings = self._collect(Rules.SAVINGS)
        self.interest_on_savings = self._collect(Rules.INTEREST_ON_SAVINGS)
        self.salary = self._collect(Rules.SALARY)
        self.salary_percent_saved = self._collect(Rules.SALARY_PERCENT_SAVED)

    def _collect(self, rule):
        value = input(rule.value.prompt)

        if is_input_valid(value, rule):
            return float(value)
        else:
            print("Invalid input")
            return self._collect(rule)

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
