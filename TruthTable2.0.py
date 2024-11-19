from colorama import *
init()
print(Fore.GREEN +'a b a|b a^b a&b ~a <<a >>a')
for a in range(2):
    for b in range(2):
        OR = a | b
        XOR = a ^ b
        AND = a & b
        NOT = ~a
        LEFT = a << 1
        RIGHT = a >> 1
        print(Fore.RED,a, Fore.BLUE,b, Fore.CYAN,OR, Fore.MAGENTA,XOR, Fore.YELLOW,AND, Fore.LIGHTCYAN_EX,NOT, Fore.LIGHTBLUE_EX,LEFT, Fore.LIGHTGREEN_EX,RIGHT)