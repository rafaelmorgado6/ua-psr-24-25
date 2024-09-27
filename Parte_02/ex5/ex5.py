#!/usr/bin/env python3

import readchar

def countNumbersUpTo(stop_char):
    num = []
    oth = {}
    order = 1
    list = []
    total_numbers = 0
    total_others = 0
    
    print("Press any keys (press 'X' to stop): ")

    while True:
        char = readchar.readchar()
        print(char)
        
        if char == stop_char:
            print("You pressed 'X', leaving....")
            break
        
        if char.isdigit():
            num.append(char)
            list.append(char)
        else:
            oth[order] = char
            order += 1
            list.append(char)

        total_numbers, total_others = isnumeric(char, total_numbers, total_others)
    
    # Explicação no final do código
    lst_comp_num = [char for char in num if char.isdigit()]

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')
    print('Total input: ' + str(list))
    print('Numbers list (ordered): ' + str(sorted(num)))
    print('Others dictionary: ' + str(oth))
    print('Numbers using list comprehensiom: ' + str(lst_comp_num))


def isnumeric(char, total_numbers, total_others):
    if char.isdigit():
        total_numbers += 1 
    else:
        total_others += 1
    return total_numbers, total_others


def main():
    countNumbersUpTo('X')

if __name__ == '__main__':
    main()



# lst_comp_num = [char for char in num if char.isdigit()]
'''
     lst_comp_num   -> Nova lista 
     char           -> O que queremos incluir na nova lista
     char in num    -> 'char' percorrerá e armazenará o valor de 'num'
     char.isdigit() -> Esta condição determina se o 'char' deve ser incluido na lista ou não
'''    
