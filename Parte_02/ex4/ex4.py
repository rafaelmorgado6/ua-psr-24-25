#!/usr/bin/env python3

import readchar

def printAllCharsUpTo():
    print("Press any key: ")

    # uso da função readchar() da biblioteca readchar
    char = readchar.readchar()  
    
    # recebe um caracter e retorna o valor ASCII (ord(A) -> 65)
    ascii_value = ord(char)

    if ascii_value < ord(" "):  # ord(" ") -> 33
        print("Por favor, insira um caractere válido (a partir do espaço).")
        return
    
    # vai desde ord(" ") até ord(char)
    for i in range(ord(" "), ascii_value +1):
        print(chr(i), end = ' ')    # chr() faz o oposto de ord(), end=' ' adiciona um espaço em branco em vez de mudar de linha
    print()

'''
def readAllUpTo(stop_char):
    print("Press any keys (press 'X' to stop): ")

    while True:
        char = readchar.readchar()
        print(char)
        
        if char == stop_char:
            print("You pressed 'X', leaving....")
            break
'''

def countNumbersUpTo(stop_char):
    total_numbers = 0
    total_others = 0
    
    print("Press any keys (press 'X' to stop): ")

    while True:
        char = readchar.readchar()
        print(char)
        
        if char == stop_char:
            print("You pressed 'X', leaving....")
            break
        
        total_numbers, total_others = isnumeric(char, total_numbers, total_others)

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')

def isnumeric(char, total_numbers, total_others):
    if char.isdigit():
        total_numbers += 1 
    else:
        total_others += 1
    return total_numbers, total_others

def main():
    printAllCharsUpTo()
    #readAllUpTo('X')
    countNumbersUpTo('X')

if __name__ == '__main__':
    main()
