import cli_headers
import validation
import calculation

def collect_input(rule):
    value = input(rule.value.prompt)

    if validation.is_input_valid(value, rule):
        value = float(value)

        return value/100 if rule.value.is_percent else value
    else:
        print("Invalid input")
        return collect_input(rule)


def main():
    cli_headers.print_program_title()

    try:
        result_months = calculation.calculate(
            collect_input(validation.Rules.HOUSE_COST),
            collect_input(validation.Rules.DOWN_PAYMENT_PERCENT),
            collect_input(validation.Rules.SAVINGS),
            collect_input(validation.Rules.INTEREST_ON_SAVINGS),
            collect_input(validation.Rules.SALARY),
            collect_input(validation.Rules.SALARY_PERCENT_SAVED),
        )
    except OverflowError as e:
        cli_headers.print_with_borders(e)
    else:
        cli_headers.print_months_as_years_and_months(result_months)

if __name__ == '__main__':
    main()
