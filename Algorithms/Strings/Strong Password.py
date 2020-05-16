#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    chars = 0
    num = False
    lChar = False
    uChar = False
    sChar = False
    i = 0
    while i<len(numbers):
        if(numbers[i] in password):
            num = True
            break
        i=i+1
    if not num:
        chars=chars+1
    i = 0
    while i<len(lower_case):
        if(lower_case[i] in password):
            lChar = True
            break
        i=i+1
    if not lChar:
        chars=chars+1
    i = 0
    while i<len(upper_case):
        if(upper_case[i] in password):
            uChar = True
            break
        i=i+1
    if not uChar:
        chars=chars+1
    i = 0
    while i<len(special_characters):
        if(special_characters[i] in password):
            sChar = True
            break
        i=i+1
    if not sChar:
        chars=chars+1

    if n+chars >=6:
        return chars
    else:
        return 6 - n
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
