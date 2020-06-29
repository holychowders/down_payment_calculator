"""
Author: https://github.com/holychowders
Forked from https://github.com/jsashbeck
"""

from time import sleep

def run_down_payment_calculator():
    """
    Calculate number of years/months of saving required to afford down payment.
    """

    success = False
    print('\nCalculate the Time Required to Save In Order to Afford Down '\
        'Payment on Dream House.\n\n'
    )

    try:
        house_cost = float(input('Enter cost of house: '))
        assert house_cost > 0, (
            'The cost of your house must be greater than 0'
        )

        down_payment_percent = (float(input(
            'Enter down payment percentage (ie, 25.2 for 25.2%): ')) / 100
        )
        assert 0 < down_payment_percent <= 1, (
            'Down payment percentage must range between 0 and 100'
        )

        savings_dollars = float(input("Enter reserved savings: "))
        assert savings_dollars >= 0, 'Reserved savings must not be negative'

        annual_salary = float(input('Enter your salary: '))
        assert annual_salary > 0, 'Salary must be greater than 0'

        annual_salary_saved_percent = (float(input(
            'Enter percentage of salary saved (ie, 25 for 25%): ')) / 100
        )
        assert 0 < annual_salary_saved_percent <= 1, (
            'Percentage salary saved must range between 0 and 100'
        )

        annual_interest_percent = float(input('Enter interest rate: ')) / 100
        assert 0 <= annual_interest_percent <= 1, (
            'Annual interest rate must range between 0 and 100'
        )

    except ValueError:
        print('\nValueError: You must enter only real number values.\a')
        return
    except AssertionError as ae:
        print(f'\nAssertionError: {ae}\a')
        return
    except Exception as e:
        print(f'\nAn error occured: {repr(e)}\a')
        return


    else:
        months = 0
        monthly_salary = annual_salary / 12
        monthly_interest_percent = annual_interest_percent / 12
        down_payment_dollars = down_payment_percent * house_cost
        monthly_salary_saved_dollars = (
            annual_salary_saved_percent * monthly_salary)

        while savings_dollars < down_payment_dollars:

            savings_dollars = (
                savings_dollars * (1 + monthly_interest_percent) +
                    monthly_salary_saved_dollars
            )

            months += 1

            if months > 1800:
                print('\nOverflowError: It would take in excess of '\
                    '150 years of saving in order to afford down payment.\a'
                )
                return

        success = True
        print('\nResult:\nYou would need to save for '\
            f'{months // 12} years, {months % 12} months'
        )

    finally:
        if success:
            print("\n\nThanks for using this calculator!")
            input('\nPress "Enter" to end: ')
            print('Goodbye!')
            sleep(2)
        else:
            input('\n\nPress "Enter" to end: ')
