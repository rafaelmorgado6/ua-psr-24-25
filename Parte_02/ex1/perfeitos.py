#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to check perfect numbers
# Eurico Pedrosa.
# PSR, September 2024.
# --------------------------------------------------

maximum_number = 100  # maximum number to test.

def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    dividers = []
    for n in range(1, value):
        if value % n == 0:
            dividers.append(n)
    return dividers
    

def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """
        
    dividers = getDividers(value)
    soma = sum(dividers)
    if soma == value:
        return True 
    elif soma != value:
        return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')
            print(getDividers(i))

if __name__ == "__main__":
    main()
