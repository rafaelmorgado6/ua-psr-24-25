#!/usr/bin/env python3

import argparse

# Criação do parser
parser = argparse.ArgumentParser(description='Exemplo de uso do argparse')

# Adicionando um argumento
parser.add_argument('--numero', type=int, help='Um número inteiro')

# Analisando os argumentos
args = parser.parse_args()

# Usando o argumento
print(f'O número fornecido é: {args.numero}')
