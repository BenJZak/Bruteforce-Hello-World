import os
import time
import colorama
from colorama import Fore, Style
import random

colorama.init()

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def print_random_color(text):
    color = random.choice(colors)
    print(color + text + Style.RESET_ALL)

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! "
target = "Hello World!"
output = ""

for i in range(len(target)):
    for char in alphabet:
        print(output, end="")
        print_random_color(char)
        if(char == target[i]):
            output += char
            break
        os.system('clear')
    os.system('clear')
    print(output)
    time.sleep(.1)
os.system('clear')
print(output)