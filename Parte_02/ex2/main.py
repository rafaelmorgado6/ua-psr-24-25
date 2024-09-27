#!/usr/bin/env python3

import my_functions

def main():
    
    print("Starting to compute prime numbers up to " + str(my_functions.maximum_number))
    
    for i in range(0, my_functions.maximum_number):
        if my_functions.isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    # __name__ is a special variable
    # Python automatically sets its value to “__main__” if the script is being run directly
    main()
   
