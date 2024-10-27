#!/usr/bin/env python3

import random
import time
import string
from collections import namedtuple
from datetime import datetime
from colorama import Fore, Style, init, Back
from pprint import pprint
import readchar
from time import sleep
from time import time

# Inicializa o Colorama
init(autoreset=True)

# Define um namedtuple para armazenar informações sobre as entradas
#Input = namedtuple('Input', ['requested', 'received', 'duration'])

# ============================= Funções Auxiliares =============================

def parse_arguments():
    """Parseia e retorna os argumentos da linha de comando."""
    import argparse
    parser = argparse.ArgumentParser(description='Definição do modo de teste de digitação')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', 
                        help='Ativa o modo de tempo para o teste (tempo máximo)')
    parser.add_argument('-mv', '--max_value', type=int, default=10, 
                        help='Número máximo de segundos ou número máximo de inputs')
    parser.add_argument('-uw', '--use_words', action='store_true', 
                        help='Ativa o modo de digitação de palavras, em vez de caracteres únicos')
    parser.add_argument('-u', '--user', type=str, default='User',  # Valor padrão "User"
                        help='Nome do usuário que está fazendo o teste')
    return parser.parse_args()

def welcome_message(user):
    """Exibe a mensagem de boas-vindas e espera o usuário iniciar."""
    print(Fore.YELLOW + f"Bem-vindo, {user}! Pressione qualquer tecla para começar o desafio...")
    readchar.readchar()

def start_test_timer(countdown=3):
    """Exibe uma contagem regressiva para iniciar o teste."""
    for i in range(1, countdown + 1):
        print(Back.YELLOW + f'Starting the test in {countdown + 1 - i} seconds', end="\r")
        sleep(1)  # pausa de 1 segundo
        print("\033[K", end="\r")  # deletes line and goes to the start of it

def get_random_character():
    """Gera uma letra minúscula aleatória."""
    return random.choice(string.ascii_lowercase)

def get_random_word_from_file(filepath='robotics.txt'):
    """Seleciona uma palavra aleatória a partir de um arquivo de texto."""
    with open(filepath, 'r') as file:
        text = file.read()
        palavras = text.split()  # Separate words with spaces
    return random.choice(palavras)

def handle_word_input(requested):
    """Captura a entrada da palavra e retorna a palavra digitada e o tempo gasto."""
    print(Fore.CYAN + f"Digite a palavra: {requested}")
    received = ""
    start_time = tic()
    
    while len(received) < len(requested):
        typed = readchar.readchar()  # Reads a char

        if typed == ' ':  # If space is hitted, program ends
            print(Back.RED + '\nTest interrupted!' + Style.RESET_ALL)
            exit()
        elif typed == '\x7f':  # Deals with backspace backspace
            if received:
                received = received[:-1]
                print('\r' + ' ' * (len(received) + 1) + '\r', end='', flush=True)  # apaga a string com o erro
                print(received, end='', flush=True) # imprime uma nova string igual à errada mas sem o erro(ultimo valor)
        else:
            received += typed
            print(typed, end='', flush=True)

    duration = toc(start_time)
    return received, duration

def handle_letter_input(requested):
    """Captura a entrada da letra e retorna a letra digitada e o tempo gasto."""
    print(Fore.CYAN + f"Digite a letra: {requested}")
    start_time = tic()
    received = readchar.readchar()
    duration = toc(start_time)
    return received, duration

def check_word_accuracy(requested, received):
    """Compara palavra esperada e recebida, e imprime resultados com cores."""
    if received == requested:
        print(Fore.GREEN + " Correto!")
        return True
    else:
        print(Fore.RED + f" Incorreto! Esperado: '{requested}'", end='\n')
        print("Seu input: ", end='')

        for i in range(len(requested)):
            if i < len(received) and requested[i] == received[i]:
                print(Fore.GREEN + received[i], end='')  
            elif i < len(received):
                print(Fore.RED + received[i], end='')  
            else:
                print(Fore.RED + "_", end='')  

        print(Style.RESET_ALL)  # Resets color style
        return False

def check_letter_accuracy(requested, received):
    """Compara letra esperada e recebida, e imprime resultados com cores."""
    if received == requested:
        print("Seu input: " + str(received) + Fore.GREEN + " Correto!")
        return True
    else:
        print("Seu input: " + str(received) + Fore.RED + f" Incorreto! Esperado: '{requested}'")
        return False

def collect_statistics(inputs, number_of_hits, test_start, current_inputs, user):
    """Calcula e imprime as estatísticas finais do teste."""
    test_end = datetime.now()
    test_duration = (test_end - test_start).total_seconds() # convert in seconds 
    accuracy = (number_of_hits / current_inputs) * 100 if current_inputs > 0 else 0  # %
    type_average_duration = sum(input.duration for input in inputs) / current_inputs if current_inputs > 0 else 0
    type_hit_average_duration = sum(input.duration for input in inputs if input.received == input.requested) / number_of_hits if number_of_hits > 0 else 0
    type_miss_average_duration = sum(input.duration for input in inputs if input.received != input.requested) / (current_inputs - number_of_hits) if current_inputs > number_of_hits else 0

    # Creates dictionary with results
    result_dict = {
        'user': user,  # Add user name
        'test_duration': test_duration,
        'test_start': test_start.strftime('%Y-%m-%d %H:%M:%S'),
        'test_end': test_end.strftime('%Y-%m-%d %H:%M:%S'),
        'number_of_types': current_inputs,
        'number_of_hits': number_of_hits,
        'accuracy_percent': accuracy,  
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration,
        'inputs': inputs,
    }

    # Prints result dictionary
    pprint(result_dict)

#Function to check if time limit has reached

def should_end_test(args, start_time, current_inputs, end_time=None):
    """Verifica se as condições de término do teste foram atingidas."""
    if args.use_time_mode and time() >= end_time:
        print(Fore.RED + "Tempo máximo atingido!")
        return True
    if current_inputs >= args.max_value:
        print(Fore.RED + "Número máximo de inputs atingido!")
        return True
    return False

# Tic and Toc functions to collect the time
def tic():
    """Retorna o tempo de início."""
    return time()

def toc(start_time):
    """Retorna o tempo decorrido desde o início."""
    return time() - start_time



