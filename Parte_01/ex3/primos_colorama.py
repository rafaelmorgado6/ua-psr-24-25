#!/usr/bin/env python3

from colorama import Fore, init, Back, Style

# Inicializa o colorama (necessário apenas no Windows)
#init(autoreset=True)

maximum_number = 10000

# Se o código encontrar qualquer número i que divide 
# value exatamente, a função retorna False imediatamente, 
# indicando que value não é primo.
def isPrime(value):
    for i in range(2,value):
        if value%i==0:
            return False
    return True
# Para um numero n, a função divide n por i, com i[1,n+1], e quando 
# encontra um valor que deixa resto 0 adiciona à lsit 'dividers'
def find_dividers(n):
    dividers = []
    for i in range(1, n+1):
        if n % i == 0:
            dividers.append(i)
    return dividers


def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))
    for i in range(0, maximum_number):
        if isPrime(i):
            print(Fore.GREEN + 'Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')
            print('Dividers (rest=0): ')
            print(find_dividers(i))
            
if __name__ == "__main__":
    # __name__ is a special variable
    # Python automatically sets its value to “__main__” if the script is being run directly
    main()
