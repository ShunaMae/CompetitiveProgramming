

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
    N, Q = map(int, input().split())
    R = sorted(list(map(int, input().split())))
    A = [0]
    for i in range(len(R)):
        A.append(A[-1]+R[i])
    
    for _ in range(Q):
        q = int(input())
        idx = bisect_right(A, q)
        print(idx-1)

main()