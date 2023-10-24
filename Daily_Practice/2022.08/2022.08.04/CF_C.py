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
    t = isint()
    for _ in range(t):
        m = isint()
        field = []
        s1 = list(ismap())
        s2 = list(ismap())
        # ジグザグ
        sec1 = 0
        seq = deque()
        s6 = deque(s1)
        s7 = deque(s2)
        s6.popleft()
        while True:
            a1 = s7.popleft()
            seq.append(a1)
            if len(s7) == 0:
                break 
            a2 = s7.popleft()
            seq.append(a2)
            a3 = s6.popleft()
            seq.append(a3)
            if len(s6) == 0:
                break
            a4 = s6.popleft()
            seq.append(a4)
        
        for i in range(len(seq)):
            if seq[i] < sec1:
                sec1 += 1 
            else:
                sec1 = max(sec1, seq[i]+1)
        # print(seq, sec1)

        # 時計回り
        sec2 = 0 
        s3 = list(reversed(s2))
        seq2 = s1 + s3
        for i in range(1, len(seq2)):
            if seq2[i] < sec2:
                sec2 += 1 
            else:
                sec2 = max(sec2, seq2[i]+1)

        # anti-clockwise 
        sec3 = s2[0] 
        s4 = list(reversed(s1))
        seq3 = s2 + s4 
        for i in range(len(seq3)-1):
            if sec3 > seq3[i]:
                sec3 += 1 
            else:
                sec3 = max(sec3, seq3[i]+1)
        
        print(min(sec1, sec2, sec3))
    
    return 
main()


                