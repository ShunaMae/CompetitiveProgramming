


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



def main():
    A, M, L, R = map(int, input().split())
    
    L -= A
    R -= A

    if L == 0:
        print(R // M + 1)
    elif R == 0:
        print(abs(L) // M + 1)
    elif L < 0 and R < 0:
        l = abs(L) // M
        r = abs(R+1) // M
        print(l-r)
    elif L > 0 and R > 0:
        l = (L-1) // M
        r = R // M
        print(r-l)
    else:
        l = abs(L)//M
        r = R // M
        print(l + r + 1)


def solve():
    A, M, L, R = map(int, input().split())
    L -= A
    R -= A

    if R <= 0:
        # 共に負なので、絶対値を取って正に戻す
        L, R  = abs(L), abs(R)
        # Lの方が0から遠いことに注意
        l = L//M
        r = (R-1)//M
        print(l-r)
    elif L < 0 < R:
        # 間に0が挟まっているので、LとRを別々に計算して足してやる
        l = abs(L)//M
        r = abs(R)//M
        print(l+r+1)
    else:
        # 共に正、一つ目の場合と同様に計算する
        # Rの方が遠いことに注意
        l = (L-1)//M
        r = R//M
        print(r-l)

solve()