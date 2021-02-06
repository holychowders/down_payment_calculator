def borders(function):
    def wrapper(*args):
        print_border()
        function(*args)
        print_border()
    return wrapper

def print_border():
    border_length = 23
    border_character = '-'
    print(border_length * border_character)

@borders
def print_with_borders(message):
    print(message)

@borders
def print_program_title():
    print("Down Payment Calculator")

@borders
def print_months_as_years_and_months(months):
    print(format_months_as_years_and_months(months))

def format_months_as_years_and_months(months):
    months_per_year = 12
    years = months // months_per_year
    months = months % months_per_year

    return f"Result: {years} years, {months} months"
