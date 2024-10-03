#!/usr/bin/env python3

from colorama import Fore, init, Back, Style
import math
from time import time
from time import time, ctime

def tic():
    global start_time
    start_time = time()                                    

def toc():
    end_time = time()
    duration = end_time - start_time
    print(f"Duração: {Fore.YELLOW}{duration:.2f} segundos")

def main():
    tic()
    for i in range(50000001):
        result = math.sqrt(i)
    toc()


if __name__ == "__main__":
    main()
   