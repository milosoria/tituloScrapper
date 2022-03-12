import sys
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format


def print_banner(title):
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    cprint(figlet_format(title, font='starwars'),
        'yellow', attrs=['bold'])

