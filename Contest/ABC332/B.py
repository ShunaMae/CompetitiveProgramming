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
from functools import lru_cache


def main():
    K, G, M = map(int, input().split())

    gc = 0
    mc = 0

    for i in range(K):
        if gc == G:
            gc = 0
        elif mc == 0:
            mc = M
        else:
            if mc + gc < G:
                gc += mc
                mc = 0
            else:
                mc = mc - (G-gc)
                gc = G
        
    
    
    print(gc, mc)

main()

