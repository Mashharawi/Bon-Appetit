
#python 3

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    a=[]
    for i in range(0,len(bill)):
        if(i!=k):
            a.append(bill[i])
    add=0
    for i in a:
        add=add+i
    if((add/2)==b):
        print("Bon Appetit")
    else:
        v=(add/2)
        print(b-int(v))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

""" output :
4 1
3 10 2 9
12
ans :5
4 1
3 10 2 9
7
ans:Bon Appetit """
