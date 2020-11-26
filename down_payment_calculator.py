#!/usr/bin/env python3
"""Calculate number of years/months of saving required to afford down payment."""

class Calculator:

    def main(self):

        self.display_program_title()

        self.house_cost = self.get_user_input("Cost of dream house: ", 1)
        self.down_payment_percent = self.get_user_input("Down payment percentage (eg, 25.2): ", 1, 100, True)
        self.savings_dollars = self.get_user_input("Savings set aside: ", 0)
        self.annual_salary = self.get_user_input("Annual salary: ", 1)
        self.annual_salary_saved_percent = self.get_user_input("Enter percentage of salary saved: ", 1, 100, True)
        self.annual_interest_percent = self.get_user_input("Enter interest rate: ", 0, 100, True)

        months_to_save = self.calculate_months_to_save()
        self.display_results(months_to_save)


    @staticmethod
    def print_newline(count=1):
        print(count * "\n", end="")


    def display_program_title(self):
        self.print_newline()
        print(23 * "-")
        print("Down Payment Calculator")
        print(23 * "-")


    def display_results(self, months_to_save):
        years_to_save = months_to_save // 12
        remainder_months_to_save = months_to_save % 12
        self.print_newline(2)
        print(f"Result: {years_to_save} years, {remainder_months_to_save} months")


    def calculate_months_to_save(self):
        # Reinitialize user inputs without 'self' for readability
        house_cost = self.house_cost
        down_payment_percent = self.down_payment_percent
        savings_dollars = self.savings_dollars
        annual_salary = self.annual_salary
        annual_salary_saved_percent = self.annual_salary_saved_percent
        annual_interest_percent = self.annual_interest_percent

        months_to_save = 0
        monthly_salary = annual_salary / 12
        monthly_interest_percent = annual_interest_percent / 12
        down_payment_dollars = down_payment_percent * house_cost
        monthly_salary_saved_dollars = annual_salary_saved_percent * monthly_salary

        is_savings_enough = savings_dollars >= down_payment_dollars
        while not is_savings_enough:
            next_months_interest_dollars = savings_dollars * (1 + monthly_interest_percent)
            savings_dollars = next_months_interest_dollars + monthly_salary_saved_dollars

            months_to_save += 1
            is_savings_enough = savings_dollars >= down_payment_dollars

            is_too_long_to_save = months_to_save > 1800  # 1800 months is 150 years
            if is_too_long_to_save:
                self.print_newline()
                print("Overflow Error: It would take in excess of "\
                    "150 years of saving in order to afford down payment.\a")
                exit()

        return months_to_save


    def get_user_input(self, message, lower_limit=None, upper_limit=None, is_percent_as_int=False):
        """
        Return converted numerical value from input.

        lower_limit/upper_limit are lower/upper numerical limit. upper_limit not accepted alone;
        Print error message when value not in range and recall self.get_user_input with same arguments.
        """
        self.print_newline()
        user_input = input(f"{message}")


        # Attempt conversion and validation.
        try:
            user_input = float(user_input)
        except ValueError as value_error:
            value_error_message = value_error.args[0]
            if "could not convert string to float" in value_error_message:
                print("Please enter a valid input \a")
            return self.get_user_input(message, lower_limit, upper_limit, is_percent_as_int)

        if lower_limit and upper_limit:
            is_user_input_valid = (lower_limit <= user_input <= upper_limit)
            if not is_user_input_valid:
                try:
                    raise ValueError(f"Please enter a number between {lower_limit} and {upper_limit}")
                except ValueError as value_error:
                    value_error_message = value_error.args[0]
                    print(f"{value_error_message} \a")
                    return self.get_user_input(message, lower_limit, upper_limit, is_percent_as_int)
        elif lower_limit:
            is_user_input_valid = (user_input >= lower_limit)
            if not is_user_input_valid:
                try:
                    raise ValueError(f"Please enter a number greater than {lower_limit}")
                except ValueError as value_error:
                    value_error_message = value_error.args[0]
                    print(f"{value_error_message} \a")
                    return self.get_user_input(message, lower_limit, upper_limit, is_percent_as_int)

        if is_percent_as_int:
            user_input_percent_as_decimal = user_input / 100
            return user_input_percent_as_decimal
        else:
            return user_input


down_payment_calculator = Calculator()
down_payment_calculator.main()
