import pyfiglet
from colorama import Fore

ascii_art = pyfiglet.figlet_format("Morpheus")
colored_ascii_art = Fore.YELLOW + ascii_art + Fore.RESET
colored_line = Fore.YELLOW + '- - - - ------------------------------ - - - -' + Fore.RESET
installer_text = Fore.RED + '               I N S T A L L E R' + Fore.RESET
print(colored_ascii_art)
print(installer_text)
print(colored_line)
