import os
import time

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! "
target = "Hello World!"
output = ""

for i in range(len(target)):
    for char in alphabet:
        print(output + char)
        if(char == target[i]):
            output += char
            break
        os.system('clear')
    os.system('clear')
    print(output)
    time.sleep(.1)
os.system('clear')
print(output)