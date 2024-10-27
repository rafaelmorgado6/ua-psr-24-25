#!/usr/bin/env python3

import random
import string
from collections import namedtuple
from datetime import datetime
from colorama import Fore, Style, init, Back
import readchar
from time import sleep, time as current_time
import signal
import sys
from my_functions import parse_arguments, welcome_message,start_test_timer,collect_statistics,check_word_accuracy
from my_functions import get_random_character,get_random_word_from_file,handle_letter_input,handle_word_input,check_letter_accuracy

init(autoreset=True)

# Defines namedtuple to collect information
Input = namedtuple('Input', ['requested', 'received', 'duration'])

# ============================= Variáveis Globais =============================
inputs = []
number_of_hits = 0
current_inputs = 0
test_start = None
user = "User"
#============================== Função Auxiliar ===============================

 # Timer interrupt handler
def handle_timeout(signum, frame):
    """Função chamada quando o tempo acaba."""
    print(Fore.RED + "\nTempo máximo atingido!")
    # Coleta e imprime as estatísticas finais
    collect_statistics(inputs, number_of_hits, test_start, current_inputs, user)
    sys.exit(0)

# Main

def main():
    global inputs, number_of_hits, current_inputs, test_start, user  # Torna global para acessar no handle_timeout

    # configuration of time alarm
    signal.signal(signal.SIGALRM, handle_timeout)

    # Arguments
    args = parse_arguments()

    # Welcome message and countdown
    user = args.user
    welcome_message(user)
    start_test_timer()

    # If time mode
    if args.use_time_mode:
        signal.alarm(args.max_value)  # Defines time alarm

    # Start of the typing test
    test_start = datetime.now()

    while True:
        if args.use_words:
            requested = get_random_word_from_file()
            received, duration = handle_word_input(requested)
            if check_word_accuracy(requested, received):
                number_of_hits += 1
            inputs.append(Input(requested, received, duration))
        else:
            requested = get_random_character()
            received, duration = handle_letter_input(requested)
            if received == ' ':
                print(Fore.RED + "Teste interrompido!")
                break
            if check_letter_accuracy(requested, received):
                number_of_hits += 1 
            inputs.append(Input(requested, received, duration))

        current_inputs += 1
        
        # Check if max inputs is hit
        if not args.use_time_mode and current_inputs >= args.max_value:
            print(Fore.RED + "Número máximo de inputs atingido!")
            break

    # Show statistics
    collect_statistics(inputs, number_of_hits, test_start, current_inputs, user)

if __name__ == '__main__':
    main()
