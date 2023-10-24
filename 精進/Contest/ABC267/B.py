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
    s = list(input())
    rows = [(0) for _ in range(7)]
    if s[0] == '1':
        return False 
    rows[0] += int(s[6])
    rows[1] += int(s[3])
    rows[2] += (int(s[7]))
    rows[2] += (int(s[1]))
    rows[3] += (int(s[4]))
    rows[4]+= (int(s[8]))
    rows[4] += (int(s[2]))
    rows[5] += (int(s[5]))
    rows[6] += (int(s[9]))
    # print(rows)

    leftest_one = -1
    rightest_one = -1
    for i in range(7):
        if rows[i] == 1:
            leftest_one = i
            break 
    for i in reversed(range(7)):
        if rows[i] == 1:
            rightest_one = i
            break
    if leftest_one == -1:
        return False
    if leftest_one == rightest_one:
        return False
    # print(leftest_one, rightest_one)
    for i in range(leftest_one, rightest_one+1):
        if rows[i] == 0:
            # print(i)
            return True 
    
    return False
         


out(main())