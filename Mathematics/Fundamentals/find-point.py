#!/bin/python3

import os
import sys

#
# Complete the findPoint function below.
#
def findPoint(px, py, qx, qy):

    my_array = [2*qx-px, 2*qy-py]
    return my_array
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        px,py,qx, qy = list(map(int,input().split()))


        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
