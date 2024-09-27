#!/usr/bin/env python3 

def isPrime(value):
    
    if value <= 1:
        return False
    
    for d in range(2,value):
        if value % d == 0:
            return False
    return True
