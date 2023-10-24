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
    r, c = ismap()
    if r == 1 or r == 15:
        return False 
    elif r ==  2 or r == 14:
        if c == 1 or c == 15:
            return False 
        else: return True 
    elif r == 3 or r == 13:
        if c == 2 or c == 14:
            return True
        else: return False
    elif r == 4 or r == 12:
        if c == 1 or c == 3 or c == 13 or c == 15:
            return False 
        else: return True
    elif r == 5 or r == 11: 
        if c == 2 or c == 4 or c == 12 or c == 14:
            return True 
        else: return False 
    elif r == 6 or r == 10:
        if c == 1 or c == 3 or c == 5 or c == 11 or c == 13 or c == 15:
            return False
        else:
            return True
    elif r == 7 or r == 9:
        if c == 2 or c == 4 or c == 6 or c == 10 or c == 12 or c == 14:
            return True
        else: return False 
    else:
        if c == 2 or c == 4 or c == 6 or c == 10 or c == 12 or c == 14 or c == 8:
            return True 
        else: return False 

if main():
    print("white")
else: print("black")    