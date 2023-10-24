# ライブラリさんたち
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
# @lru_cache(maxsize=None)

# 便利な関数くん
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def out(func):
    if func: print("Yes")
    else: print("No")
import sys
def input(): return sys.stdin.readline()[:-1]
def isint(): return int(input())
def ismap(): return map(int, input().split())
def issmap(): return map(str, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]
def iszero(): return list(map(lambda x: int(x) - 1, input().split()))
def sout(list):
    for i in list:
        print(i)

# run-length 
# A = [(k, len(list(g))) for k, g in groupby(map(int, input().split()))]

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 16


def main():
    N, L, R = ismap()
    A = list(ismap())
    B = list(accumulate(A))
    m = sum(A)
    for x in range(N+1):
        for y in range(N+1):
            if x == 0:
                res = N - y - 1 
                t = B[res] + y * R
                m = min(t, m)
            elif y == 0:
                res = B[-1] - B[x-1]
                t = res + L * x
                m = min(m, t)
            elif x + y == N:
                t = L * x + R * y
                m = min(m, t)
            elif x < (N-y):
                res = B[N-y-1] - B[x-1]
                t = res + x * L + y * R 
                m = min(m, t)
            else:
                res = N - y 
                t = res * L + y * R
                m = min(m, t)
    
    return m 

print(main())



