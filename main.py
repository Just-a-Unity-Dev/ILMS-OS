# Imports
from inspect import isclass
from colorama import Fore, Back, Style
import ilmsl

running = True

while running:
	input = input(f"{Fore.GREEN}{ilmsl.pwd()}:{Style.RESET_ALL} ")