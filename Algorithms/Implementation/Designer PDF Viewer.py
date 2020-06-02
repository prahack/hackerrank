#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxH = min(h)
    i = 0
    while h != max(h) and i<len(word):
        if(h[string.ascii_lowercase.index(word[i])] > maxH):
            maxH = h[string.ascii_lowercase.index(word[i])]
        i = i + 1
    return maxH * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
