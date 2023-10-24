# ライブラリさんたち
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd, log2, log10

# 便利な関数くん
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def out(func):
    if func: print("Yes")
    else: print("No")
def isint(): return int(input())
def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1


def main():
    N, X, Y = ismap()
    if N == 1:
        return 0
    red = 1 
    blue = 0
    red_level = N
    blue_level = 0
    while True:
        if red_level == 1 and blue_level == 1:
            break 

        if red_level >= 2:
            blue_level = red_level
            red_level -= 1 
            blue += red * X

        
        if blue_level >= 2:
            blue_level -= 1 
            red_level = blue_level
            red += blue
            blue = blue * Y
        
        # print(blue)
    
    return blue 

print(main())

        