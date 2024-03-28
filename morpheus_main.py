from colorama import Fore
import pyfiglet

def morpheus_banner():
    ascii_art = pyfiglet.figlet_format("Morpheus")
    colored_ascii_art = Fore.YELLOW + ascii_art + Fore.RESET
    colored_line = Fore.YELLOW + '- - - - ------------------------------ - - - -' + Fore.RESET
    installer_text = Fore.RED + '               I N S T A L L E R' + Fore.RESET
    print(colored_ascii_art)
    print(installer_text)
    print(colored_line)

# Call the function to display the Morpheus banner
morpheus_banner()

