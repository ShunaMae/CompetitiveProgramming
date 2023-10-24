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
    S = list(str(input()))
    # 先頭の文字が大文字のAであるかの確認
    if not S[0] == 'A':
        return False 
    # Sの先頭から3文字目と末尾から2文字目の間に大文字のCはちょうど一個含まれるかの確認
    if not S[2:-1].count('C') == 1:
        return False 
    # A,Cを除く全ての文字が小文字であることの確認
    capital = 0
    for i in range(1, len(S)):
        if S[i].isupper():
            capital += 1 
    if not capital == 1:
        return False 
    
    return True 

if main():
    print("AC")
else:
    print('WA')

    

    

