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
    n, p, q, r = ismap()
    A = list(ismap())
    a = list(accumulate(A))
    b = list(accumulate(reversed(A)))
    # print(a)
    p_limit = n - bisect_right(b, (q+r)) 
    q_limit = n - bisect_right(b, r)
    # print(p_limit)
    start = 0
    end = 1
    for i in range(p_limit):
        if a[end] - a[start] == p:
            q_start = end
            q_end = q_start + 1
            # print(start, end, "p")
            for j in range(i+1, q_limit):
                if a[q_end] - a[q_start] == q:
                    r_start = q_end 
                    r_end = r_start + 1
                    # print(r_start, r_end, 'r')
                    for k in range(j+1, n):
                        if a[r_end] - a[r_start] == r:
                            return True
                        elif a[r_end] - a[r_start] < r and r_end <= n-2:
                            r_end += 1 
                        else:
                            continue 
                elif a[q_end] - a[q_start] < q:
                    q_end += 1 
                else: continue 
        elif a[end] - a[start] < p:
            end += 1 
            # print(start, end, 'small')
        else:
            start += 1 
            end += 1 
            # print(start, end, 'large')
    return False


out(main())




