# Write a program that prints all prime numbers. 
# (Note: if your programming language does not support arbitrary size numbers, 
# printing all primes up to the largest number you can easily represent is fine too.)

import time
starttime = time.time()
START = 2
MAX = 1000
primes=[]
z = 1

for x in range(START, MAX):
    isprime = True
    for y in primes:
        if y > x/z:
            print("again \n", y, x)
            break
        if x%y == 0:
            isprime = False
            break
        z=y
    if(isprime):  
        primes.append(x)
print(primes)
print("time", time.time() - starttime)