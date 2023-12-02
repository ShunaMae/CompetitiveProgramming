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
    N = is_int()
    A = list(is_map(int))
    d = defaultdict(int)
    for i in A:
        d[i] += i

    d = sorted(d.items())
    d.append((10**6+1, 0))
    d.append((10**6+2, 0))

    li = [[] for _ in range(len(d))]
    for i in reversed(range(len(d)-2)):
        num, s1, s2 = d[i][0], d[i][1], d[i+1][1]
        li[i].append(num)
        li[i-1].append(s1+s2)
    print(d)
    li[-2].append(0)
    print(li)
    d_updated = dict(li[:-1])

    
    ans = []
    for j in A:
        ans.append(d_updated[j])

    
    print(li)
    print(d_updated)
    print(*ans)
main()