#!/usr/bin/env python3
"""Calculate number of years/months of saving required to afford down payment."""

EXIT_KEYWORD = "exit"
RESTART_KEYWORD = "rerun"


def main():
    print_newline()
    print(23 * "-")
    print("Down Payment Calculator")
    print(23 * "-")
    print(f"Type '{EXIT_KEYWORD}' or '{RESTART_KEYWORD}' at any time")
    print_newline()


    house_cost = get_user_input("Cost of dream house: ", 1)
    down_payment_percent = get_user_input("Down payment percentage (eg, 25.2): ", 1, 100, True)
    savings_dollars = get_user_input("Savings set aside: ", 0)
    annual_salary = get_user_input("Annual salary: ", 1)
    annual_salary_saved_percent = get_user_input("Enter percentage of salary saved: ", 1, 100, True)
    annual_interest_percent = get_user_input("Enter interest rate: ", 0, 100, True)

    months_to_save = 0
    monthly_salary = annual_salary / 12
    monthly_interest_percent = annual_interest_percent / 12
    down_payment_dollars = down_payment_percent * house_cost
    monthly_salary_saved_dollars = (
        annual_salary_saved_percent * monthly_salary)

    # Calculate and print result
    is_savings_enough = savings_dollars >= down_payment_dollars
    while not is_savings_enough:
        next_months_interest_dollars = (
            savings_dollars * (1 + monthly_interest_percent)
        )
        savings_dollars = (next_months_interest_dollars +
            monthly_salary_saved_dollars
        )
        months_to_save += 1
        is_savings_enough = savings_dollars >= down_payment_dollars
        is_too_long_to_save = months_to_save > 1800  # 1800 months is 150 years
        if is_too_long_to_save:
            print_newline()
            print("Overflow Error: It would take in excess of "\
                "150 years of saving in order to afford down payment.\a"
            )
            get_user_input(f"Type '{RESTART_KEYWORD}' to restart or type '{EXIT_KEYWORD}' to end: ", at_program_end=True)

    years_to_save = months_to_save // 12
    remainder_months_to_save = months_to_save % 12
    print_newline(2)
    print(f"Result: {years_to_save} years, {remainder_months_to_save} months")
    print_newline(2)


    get_user_input(f"Type '{RESTART_KEYWORD}' to restart or type '{EXIT_KEYWORD}' to end: ", at_program_end=True)


def print_newline(count=1):
    print(count * "\n", end="")


def get_user_input(message, lower_limit=None, upper_limit=None, is_percent_as_int=False, at_program_end=False):
    """
    Return converted numerical value from input if not request to exit or restart main.

    lower_limit/upper_limit are lower/upper numerical limit. upper_limit not accepted alone;
    Execute requests to restart or exit.
    Print error message when value not in range and recall get_user_input with same arguments.
    """
    print_newline()
    user_input = input(f"{message}")

    user_wants_to_exit = (user_input == EXIT_KEYWORD)
    user_wants_to_restart = (user_input == RESTART_KEYWORD)
    if user_wants_to_exit: exit()
    elif user_wants_to_restart:
        print_newline(2)
        main()

    # If at end, accept only the above keywords.
    if at_program_end: return get_user_input(f"{message}\a", at_program_end=True)

    # Attempt conversion and validation.
    try:
        user_input = float(user_input)

        if lower_limit != None:
            if upper_limit:
                is_user_input_valid = (lower_limit <= user_input <= upper_limit)
                if not is_user_input_valid:
                    raise ValueError(f"Please enter a number between {lower_limit} and {upper_limit}")
            is_user_input_valid = (user_input >= lower_limit)
            if not is_user_input_valid:
                raise ValueError(f"Please enter a number greater than {lower_limit}")

        if is_percent_as_int:
            percent_int_as_decimal = user_input/100
            return percent_int_as_decimal
        else: return user_input

    except ValueError as ve:
        if "could not convert string to float" in ve.args[0]:
            print("Please enter a valid input \a")
        else: print(f"{ve} \a")

        return get_user_input(message, lower_limit, upper_limit, is_percent_as_int)


main()
