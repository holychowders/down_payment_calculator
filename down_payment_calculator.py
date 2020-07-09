#!/usr/bin/env python3
"""Calculate number of years/months of saving required to afford down payment."""

EXIT_KW = "exit"
RESTART_KW = "rerun"


def newline(count=1):
    """Print a number, count, of newlines. Use outside of print statements."""
    print(count * "\n", end="")


def prompt(msg, gt=None, Lt=None, percent=False, finished=False):
    """
    Return converted numerical value from input if not request to exit or restart main.

    gt/Lt are lower/upper numerical limit. Lt not accepted alone;
    Execute requests to restart or exit.
    Print error message when value not in range and recall prompt with same arguments.
    """
    newline()
    val = input(f"{msg}")

    # Check input for command keywords and execute if present.
    if val == EXIT_KW: exit()
    elif val == RESTART_KW:
        newline(2)
        main()

    # If at end, accept only the above keywords.
    if finished: return prompt(f"{msg} \a", finished=True)

    # Attempt conversion and validation.
    try:
        val = float(val)

        if gt != None:
            if Lt and not (gt <= val <= Lt):
                raise ValueError(f"Please enter a number between {gt} and {Lt}")
            if not (val >= gt):
                raise ValueError(f"Please enter a number greater than {gt}")

        if percent: return val/100
        else: return val

    except ValueError as ve:
        if "could not convert string to float" in ve.args[0]:
            print("Please enter a valid input \a")
        else: print(f"{ve} \a")

        return prompt(msg, gt, Lt, percent)


def main():
    """Calculate number of years/months of saving required to afford down payment."""

    newline()
    print(23 * "-")
    print("Down Payment Calculator")
    print(23 * "-")
    print(f"Type '{EXIT_KW}' or '{RESTART_KW}' at any time")
    newline()


    house_cost = prompt("Cost of dream house: ", 1)
    down_payment_percent = prompt("Down payment percentage (eg, 25.2): ", 1, 100, True)
    savings_dollars = prompt("Savings set aside: ", 0)
    annual_salary = prompt("Annual salary: ", 1)
    annual_salary_saved_percent = prompt("Enter percentage of salary saved: ", 1, 100, True)
    annual_interest_percent = prompt("Enter interest rate: ", 0, 100, True)

    months = 0
    monthly_salary = annual_salary / 12
    monthly_interest_percent = annual_interest_percent / 12
    down_payment_dollars = down_payment_percent * house_cost
    monthly_salary_saved_dollars = (
        annual_salary_saved_percent * monthly_salary)

    # Calculate and print result
    while savings_dollars < down_payment_dollars:
        savings_dollars = (
            savings_dollars * (1 + monthly_interest_percent) +
                monthly_salary_saved_dollars
        )
        months += 1
        if months > 1800:
            newline()
            print("Overflow Error: It would take in excess of "\
                "150 years of saving in order to afford down payment.\a"
            )
            prompt(f"Type '{RESTART_KW}' to restart or type '{EXIT_KW}' to end: ", finished=True)

    newline(2)
    print(f"Result: {months // 12} years, {months % 12} months")
    newline(2)


    prompt(f"Type '{RESTART_KW}' to restart or type '{EXIT_KW}' to end: ", finished=True)


main()
