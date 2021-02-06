import cli_headers
import validate_inputs
import calculation

class Inputs:
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
            if rule.value.is_percent:
                return (float(value) / 100)
            else:
                return float(value)
        else:
            print("Invalid input")
            return self._collect(rule)


def main():
    cli_headers.print_program_title()

    inputs = Inputs()
    inputs.collect()

    try:
        result_months = calculation.calculate(
            inputs.house_cost, inputs.down_payment_percent,
            inputs.savings, inputs.interest_on_savings,
            inputs.salary, inputs.salary_percent_saved
        )
    except OverflowError as e:
        cli_headers.print_with_borders(e)
    else:
        cli_headers.print_months_as_years_and_months(result_months)

if __name__ == '__main__':
    main()
