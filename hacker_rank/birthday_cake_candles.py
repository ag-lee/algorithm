import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort(reverse=True);
    tallest = ar[0]
    count = 0
    for ele in ar:
        if tallest == ele:
            count += 1
        else:
            break;

    return count
