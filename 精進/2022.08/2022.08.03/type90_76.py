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

# 円環
# 方針としては、累積和＋二分探索
def main():
    N = isint()
    A = list(ismap())
    # そもそも１０で割れないならば無理
    if sum(A) % 10 != 0:
        return False 
    # ゴールとなる数字
    goal = sum(A) // 10 
    # リストを二倍しておく
    A_doubled = A * 2 
    # 累積和
    accumulated_list = list(accumulate(A_doubled))
    # 探索用のset 
    accumulated_set = set(accumulated_list)
    # それぞれに対して決め打ち二分探索
    for i in range(N):
        reach = accumulated_list[i] + goal
        if reach in accumulated_set:
            return True 
    
    return False 

out(main())

    

