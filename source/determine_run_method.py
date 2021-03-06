import sys

import cli_main
import gui_main

def determine_run_method():
    try:
        first_cli_argument = sys.argv[1]
    except IndexError:
        first_cli_argument = None

    if first_cli_argument == 'cli':
        return cli_main
    else:
        return gui_main
