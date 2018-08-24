from math import *

def checkprime(num):
    if num <= 2:
        return False
    if num == 2:
        return True
    for i in range(3,ceil(sqrt(num)),2):
        if num % i == 0:
            return False
    return True

number = int(input("give me a number: "))
print(checkprime(number))
