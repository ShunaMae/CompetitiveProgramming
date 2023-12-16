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
    N = int(input())
    rep = [int("1"*i) for i in range(1, 100)]
    ans = []
    for i in range(len(rep)):
        for j in range(len(rep)):
            for k in range(len(rep)):
                ans.append(rep[i]+rep[j]+rep[k])
    
    ans = sorted(list(set(ans)))
    print(ans[N-1])

main()
