#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    e=arr[-1]
    arr[-1]=arr[-2]
    i=n-2
    while True:
        print(*arr,sep=' ')
        if arr[i-1]>e and i>0:
            arr[i]=arr[i-1]
            i-=1
        else:
            arr[i]=e
            print(*arr,sep=' ')
            break
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
