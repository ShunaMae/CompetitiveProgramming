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
    N, S, K = map(int, input().split())
    cost = 0
    for _ in range(N):
        p, q = map(int, input().split())
        cost += p * q
    
    if cost >= S:
        print(cost)
    else:
        print(cost+K)

main()