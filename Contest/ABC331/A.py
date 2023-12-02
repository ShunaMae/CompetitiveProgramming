## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

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
from functools import lru_cache

def main():
    M, D = map(int, input().split())
    y, m, d = is_map(int)

    if d == D:
        print(y, m, d+1)
    else:
        if m == M:
            print(y+1, 1, 1)
        else:
            print(y, m+1, 1)

main()