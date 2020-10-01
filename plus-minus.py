#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zero=0
    positive=0
    negative=0
    for i in arr:
        if i==0:
            zero+=1
        if i<0:
            negative+=1
        if i>0:
            positive+=1
    
    zratio=format(zero/len(arr), '.6f')
    pratio=format(positive/len(arr), '.6f')
    nratio=format(negative/len(arr), '.6f')
    

    print(pratio)
    print(nratio)
    print(zratio)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
