# Trying to generate prime numbers..........
# With a python script.
#
# :)

import time

INIT = 1 # The first prime

def is_prime(number):

    ''' Trying
    to check if the number is a prime
    '''


    if number == 0:
        return "Number 0, not prime"

    if number == 1:
        return "Number 1, first prime"

    if number == 2:
        return "True  prime, number 2"

  
       
    c = 2
    flag = True
    while c < number:

        if (number % c) != 0:
            c += 1
            continue

        if (number % c) == 0:
            flag = False
            break



    return flag




start = time.clock()
for x in range(100000):

    print("Broj: " + str(x) + ": " + str(is_prime(x)) + " prime number")

end = time.clock()
print("Proteklo vrijeme: " + str(end-start))
