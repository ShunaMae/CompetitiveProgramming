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
MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 16

# いくつか選ぶ方法のうち、その平均値がちょうど整数となるものが何通りあるかを求めよ。

# k個選ぶとき、和がkの倍数 (Sk)
# dp[i][k][s]: 最初のi個からk個選んだ時に総和がk*sになるものが何個あるか
# A[i]を選ばない場合: dp[i+1][k][s] += dp[i][k][s]
# 選ぶ場合: dp[i+1][k+1][(k*s + A[i]) / (k+1)] += dp[i][k][s]




def main():
    N = isint()
    A = list(ismap())
    ans = N
    for i in range(2, N+1):
        new_A = [(j % i) for j in A]
        if sum(new_A) == 0:
            ans += N
        else:
            dp = [[(0) for _ in range(sum(new_A))] for _ in range(N)]
            dp[0][0] = 1
            for i in range(N-1):
                for s in range(sum(new_A)):
                    dp[i+1][s] += dp[i][s]
                    if (s + new_A[i]) < sum(new_A):
                        dp[i+1][s + new_A[i]] += dp[i][s]
            for k in range(N):
                ans += dp[k][sum(new_A)-1]
    
    return ans % MOD

print(main())





