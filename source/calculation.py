MONTHS_PER_YEAR = 12
MAX_MONTHS_TO_SAVE = 1800  # 1800 months is 150 years
OVERFLOW_ERROR_MSG = (f"Overflow Error: It would take too long to save.")

class Calculation:
    def __init__(
            self,
            house_cost, down_payment_percent,
            savings, interest_on_savings,
            salary, salary_percent_saved
            ):

        self.house_cost = house_cost
        self.down_payment_percent = down_payment_percent
        self.savings = savings
        self.interest_on_savings = interest_on_savings
        self.salary = salary
        self.salary_percent_saved = salary_percent_saved

        self.initialize_calculation_variables()

    def initialize_calculation_variables(self):
        self.result_months = 0

        self.down_payment_amount = self.down_payment_percent * self.house_cost
        self.monthly_interest = self.interest_on_savings / MONTHS_PER_YEAR
        self.monthly_salary = self.salary / MONTHS_PER_YEAR
        self.monthly_salary_savings = self.salary_percent_saved * self.monthly_salary

    def calculate(self):
        while not self.is_savings_enough():
            self.result_months += 1

            if self.will_take_too_long_to_save():
                raise OverflowError(OVERFLOW_ERROR_MSG)

            self.calculate_next_months_savings()

        return self.result_months

    def calculate_next_months_savings(self):
        savings_from_interest = self.savings * (1 + self.monthly_interest)
        self.savings = self.monthly_salary_savings + savings_from_interest

    def is_savings_enough(self):
        return self.savings >= self.down_payment_amount

    def will_take_too_long_to_save(self):
        return self.result_months >= MAX_MONTHS_TO_SAVE
