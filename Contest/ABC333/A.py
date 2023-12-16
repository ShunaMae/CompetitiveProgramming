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

def threethree():
    s = list(input())
    if len(set(s))==1:
        print("Yes")
    else:
        print("No")

def main():
    N = int(input())
    ans = ""
    for i in range(N):
        ans += str(N)
    
    print(ans)
main()