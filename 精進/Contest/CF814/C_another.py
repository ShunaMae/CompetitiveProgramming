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

# false : tonya 
# true burenka 
def solve():
    n, q = ismap()
    a = list(ismap())
    max_a = max(a)
    max_a_ind = a.index(max_a)
    a = deque([(i+1, a[i]) for i in range(n)])
    x = [[] for i in range(n)]
    for j in range(1, n+1):
        c1_ind, c1 = a.popleft()
        c2_ind, c2 = a.popleft()
        if c1 > c2:
            a.appendleft((c1_ind, c1))
            a.append((c2_ind, c2))
            x[c1_ind-1].append(j)
        else:
            a.appendleft((c2_ind, c2))
            a.append((c1_ind, c1))
            x[c2_ind-1].append(j)
    
    for _ in range(q):
        i, k = ismap()
        i -= 1 
        if k < n:
            ind = bisect_right(x[i], k)
            # print(x[i], "this is it")
            print(ind)
        else:
            if i == max_a_ind:
                print(len(x[i]) + (k-n))
            else:
                print(len(x[i]))

for _ in range(isint()):
    solve()
    




    
