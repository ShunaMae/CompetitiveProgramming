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
    N, S, M, L = is_map(int)
    dp = [(10**18) for _ in range(10**5)]
    dp[0] = 0
    
    for i in range(10**4):
        dp[i+6] = min(dp[i+6], dp[i]+S)
        dp[i+8] = min(dp[i+8], dp[i]+M)
        dp[i+12] = min(dp[i+12], dp[i]+L)

    for more_eggs in range(N, len(dp)):
        if dp[more_eggs] != 10**18:
            print(dp[more_eggs])
            return
        

main()