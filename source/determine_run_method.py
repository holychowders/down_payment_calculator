import sys

import cli_main
import gui_main

def determine_run_method():
    try:
        first_cli_argument = sys.argv[1]  # sys.argv[0] would be the name of the program, not the actual first argument.
    except IndexError:
        first_cli_argument = None

    if not first_cli_argument:
        return gui_main
    elif first_cli_argument == 'gui':
        return gui_main
    elif first_cli_argument == 'cli':
        return cli_main
    else:
        return gui_main
