import math
from numpy import number

n = int(input())

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3,int(math.sqrt(n)) + 1, 2):
     if number % i == 0:
        return False
        return True
    
if is_prime(n):
    print("IT IS A PRIME")
else:
    print("IT IS NOT A PRIME")