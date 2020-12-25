#!/usr/bin/env python3
import headers
from inputs import Inputs
from calculation import Calculation

def main():
    headers.print_program_title()

    inputs = Inputs()
    inputs.collect_inputs()

    calculation = Calculation(
        inputs.house_cost, inputs.down_payment_percent,
        inputs.savings, inputs.interest_on_savings,
        inputs.salary, inputs.salary_percent_saved)
    try:
        result = calculation.calculate()
    except OverflowError as e:
        headers.print_with_borders(e)
    else:
        headers.print_months_as_years_and_months(result)


if __name__ == "__main__":
    main()
