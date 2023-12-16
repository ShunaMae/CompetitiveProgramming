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

import sys
sys.setrecursionlimit(10 ** 6)

# 頂点 v を根とする部分木を探索
# p := 頂点 v の親
# siz[v] := 頂点 v を根とする部分木のサイズ
# chs[v] := 頂点 v の子頂点のリスト
def rec(v, p, siz, chs):
    # 頂点 v の各子頂点を探索
    for ch in chs[v]:
        # 子頂点 ch を根とした部分木を再帰的に探索
        # 子頂点 ch の親は v である
        rec(ch, v, siz, chs)

    # 帰りがけ時に答えを合算する
    siz[v] = 1
    for ch in chs[v]:
        siz[v] += siz[ch]

def main():
    N = int(input())
    G = [[] for i in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    
    print(G)

    if len(G[1]) == 1:
        print(1)
        return
    
    siz = [0] * (N)
    rec(0, -1, siz, G)

    print(siz)

main()

