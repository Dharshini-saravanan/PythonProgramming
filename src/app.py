import calculator 
import colorama 
from colorama import Fore, Back, Style, init 

init(autoreset=True)
result=(calculator.multiply(5,2)) 
print(Fore.RED + "Multiplication is: ",result)

result=(calculator.add(7,2))
print(Fore.YELLOW + "Addition is: " + Fore.BLUE + str(result))

result+(calculator.sub(8,5))
print(Back.CYAN + Fore.GREEN + "Subration is: "+Back.CYAN + Fore.GREEN + str(result))
