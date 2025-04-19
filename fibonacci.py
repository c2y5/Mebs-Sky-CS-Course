from colorama import Fore
import time
import sys

menuT = Fore.CYAN + """
███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                      
"""+Fore.RESET

title = Fore.CYAN + """
███████╗██╗██████╗  ██████╗ ███╗   ██╗ █████╗  ██████╗ ██████╗██╗
██╔════╝██║██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██╔════╝██╔════╝██║
█████╗  ██║██████╔╝██║   ██║██╔██╗ ██║███████║██║     ██║     ██║
██╔══╝  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║██║     ██║     ██║
██║     ██║██████╔╝╚██████╔╝██║ ╚████║██║  ██║╚██████╗╚██████╗██║
╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚═╝
                                                                 
""" + Fore.RESET

def calculate_factorial():
    print(Fore.CYAN + """
███████╗ █████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗     
██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║     
█████╗  ███████║██║        ██║   ██║   ██║██████╔╝██║███████║██║     
██╔══╝  ██╔══██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║██║     
██║     ██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝
                                                                     
""" + Fore.RESET)
    
    print(Fore.LIGHTYELLOW_EX + "Enter a number to calculate its factorial: " + Fore.RESET)
    try:
        num = int(input(Fore.RESET + "Number: " + Fore.RESET))
        if num < 0:
            print(Fore.RED + "Please enter a positive number" + Fore.RESET)
            return
        result = 1
        for x in range(1, num + 1):
            result *= x
        print(Fore.GREEN + f"The factorial of {Fore.WHITE + str(num) + Fore.GREEN} is {Fore.WHITE + str(result)}" + Fore.RESET)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid number." + Fore.RESET)

def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    sys.stdout.write(f'[{Fore.GREEN}%s{Fore.RESET}] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()

def calculate_fibonacci():
    print(title)
    amt = input(Fore.LIGHTYELLOW_EX + "Enter the number of Fibonacci numbers to generate: " + Fore.RESET)
    if amt.isdigit() and int(amt) > 0:
        amt = int(amt)
    else:
        print(Fore.RED + "Please enter a valid positive number." + Fore.RESET)
        return
    
    print(Fore.LIGHTYELLOW_EX + "Generating Fibonacci numbers..." + Fore.RESET)
    for x in range(11):
        time.sleep(0.05)
        progressBar(x, 10)
    
    print("\n")

    fibSeq = [0, 1]

    for x in range(2, amt):
        fibSeq.append(fibSeq[x - 1] + fibSeq[x - 2])

    for x in fibSeq:
        print(f"> {x}")

    input(Fore.RESET + "\nPress Enter to continue..." + Fore.RESET)

def menu():
    print(menuT)
    print(Fore.RESET +
        f"1. {Fore.GREEN}Calculate {Fore.LIGHTYELLOW_EX}Factorial\n" 
        f"{Fore.RESET}2. {Fore.GREEN}Calculate {Fore.LIGHTYELLOW_EX}Fibonacci\n"
        f"{Fore.RESET}3. {Fore.RED}Exit\n" + Fore.RESET
    )

    choice = input(Fore.RESET + "Enter your choice: " + Fore.RESET)
    if choice == '1':
        calculate_factorial()
        menu()
    elif choice == '2':
        calculate_fibonacci()
        menu()
    elif choice == '3':
        print(Fore.RED + "Exiting..." + Fore.RESET)
        sys.exit(0)
    else:
        print(Fore.RED + "Invalid choice. Please try again." + Fore.RESET)
        menu()

menu()