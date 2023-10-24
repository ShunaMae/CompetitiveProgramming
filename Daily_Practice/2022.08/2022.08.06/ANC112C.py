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
INF = 10 ** 16


def main():
    N = isint()
    info = []
    for _ in range(N):
        x, y, h = ismap()
        info.append([x,y,h]) 
    for cx in range(32, 33):
        for cy in range(0,1):
            same = True
            h = -1
            for point in range(N):
                if info[point][2] != 0:
                    temp_h = info[point][2] + abs(info[point][0] - cx) + abs(info[point][1] - cy)
                    if h == -1:
                        h = temp_h
                    else:
                        same = same and (temp_h == h) and (h > 0)
                else:
                    height = max(0, h - abs(info[point][0] - cx) - abs(info[point][1] - cy))
                    print(height)
                    if height != 0:
                        same = False 
                    else:
                        continue
            if same:
                print(cx, cy, h)
                break 
    return 

main()