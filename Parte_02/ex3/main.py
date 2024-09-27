#!/usr/bin/env python3

import my_functions
import argparse
from colorama import Fore, init, Back, Style

def main():
    
    # Cria um novo objeto parser que irá processar os argumentos passados na linha de comando
    parser = argparse.ArgumentParser(description='Compute the prime numbers up to the max_number')

    # Adiciona um argumento chamado --max_number que é esperado na linha de comando.
    parser.add_argument('--max_number', type=int, help='O número máximo até onde calcular números primos')
    
    # Analisa os argumentos fornecidos na linha de comando e os armazena em um objeto args
    args = parser.parse_args()

    # Armazena o valor fornecido pelo usuário para --max_number em uma variável local max_number.
    max_number = args.max_number

    # Imprime todos os argumentos analisados, incluindo o valor de max_number
    print(args)


    print("Starting to compute prime numbers up to " + str(max_number))
    
    for i in range(0, max_number):
        if my_functions.isPrime(i):
            print(Fore.GREEN + 'Number ' + str(i) + ' is prime.')
        else:
            print(Fore.RED + 'Number ' + str(i) + ' is not prime.')


if __name__ == "__main__":
   
    main()
