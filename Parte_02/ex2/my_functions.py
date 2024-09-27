maximum_number = 10000

def isPrime(value):
    for i in range(2,value):
        if value%i==0:
            return False
        
    return True
