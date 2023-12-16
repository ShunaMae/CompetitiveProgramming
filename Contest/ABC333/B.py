## frequently used functions 
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache, reduce 


def main():
    one = ["AB", "BC", "CD", "DE", "EA", "AE", "ED", "DC", "CB", "BA"]
    two = ["AC", "CA","AD", "DA", "BE", "EB", "BD", "DB", "CE", "EC"]

    S = input()
    T = input()

    if (S in one and T in one) or (S in two and T in two):
        print("Yes")
    else:
        print("No")

main()