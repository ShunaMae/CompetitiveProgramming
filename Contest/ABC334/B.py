


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
    A, M, L, R = map(int, input().split())
    
    L -= A
    R -= A

    if L == 0:
        print(R // M + 1)
    elif R == 0:
        print(abs(L) // M + 1)
    elif L < 0 and R < 0:
        l = abs(L) // M
        r = abs(R+1) // M
        print(l-r)
    elif L > 0 and R > 0:
        l = (L-1) // M
        r = R // M
        print(r-l)
    else:
        l = abs(L)//M
        r = R // M
        print(l + r + 1)
main()