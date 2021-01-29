import validate_inputs

class InputsFromPrompt:
    def collect(self):
        self.house_cost = self._collect(validate_inputs.Rules.HOUSE_COST)
        self.down_payment_percent = self._collect(validate_inputs.Rules.DOWN_PAYMENT_PERCENT)
        self.savings = self._collect(validate_inputs.Rules.SAVINGS)
        self.interest_on_savings = self._collect(validate_inputs.Rules.INTEREST_ON_SAVINGS)
        self.salary = self._collect(validate_inputs.Rules.SALARY)
        self.salary_percent_saved = self._collect(validate_inputs.Rules.SALARY_PERCENT_SAVED)

    def _collect(self, rule):
        value = input(rule.value.prompt)

        if validate_inputs.is_input_valid(value, rule):
            return float(value)
        else:
            print("Invalid input")
            return self._collect(rule)
