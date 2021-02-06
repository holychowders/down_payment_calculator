MONTHS_PER_YEAR = 12
MAX_MONTHS_TO_SAVE = 1800  # 1800 months is 150 years
OVERFLOW_ERROR_MSG = (f"Overflow Error: It would take too long to save.")

def calculate(
        house_cost, down_payment_percent,
        current_savings, interest_on_savings,
        salary, salary_percent_saved
    ):
    result_months = 0

    down_payment_amount = down_payment_percent * house_cost
    monthly_interest = interest_on_savings / MONTHS_PER_YEAR
    monthly_salary = salary / MONTHS_PER_YEAR
    monthly_salary_savings = salary_percent_saved * monthly_salary

    while not is_savings_enough(current_savings, down_payment_amount):
        result_months += 1

        if will_take_too_long_to_save(result_months, MAX_MONTHS_TO_SAVE):
            raise OverflowError(OVERFLOW_ERROR_MSG)

        current_savings = calculate_next_months_savings(
            current_savings, monthly_interest, monthly_salary_savings
        )

    return result_months

def calculate_next_months_savings(current_savings, monthly_interest, monthly_salary_savings):
    savings_from_interest = current_savings * (1 + monthly_interest)
    return monthly_salary_savings + savings_from_interest

def is_savings_enough(current_savings, required_savings):
    return current_savings >= required_savings

def will_take_too_long_to_save(time_will_take, minimum_time_required):
    return time_will_take >= minimum_time_required
