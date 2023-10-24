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
    N, X, Y, Z = ismap()
    A = list(ismap())
    B = list(ismap())
    students = []
    for i in range(N):
        students.append([i, A[i], B[i], A[i]+B[i]])
    students_sort= sorted(students, key = itemgetter(0))
    students_sort = sorted(students_sort, key = itemgetter(1), reverse = True)
    seen = isseen(N)
    
    for j in range(X):
        ind = students_sort[j][0]
        seen[ind] = True
    # print(seen)
    english = sorted(students_sort[X:], key = itemgetter(0))
    english = sorted(english, key = itemgetter(2), reverse = True)
    for j in range(Y):
        ind = english[j][0]
        seen[ind] = True 


    both = []
    for x in range(N):
        if not seen[x]:
            both.append(students[x])
    
    both = sorted(both, key = itemgetter(0))
    both = sorted(both, key = itemgetter(3), reverse = True)
    
    for k in range(Z):
        ind = both[k][0]
        seen[ind] = True
    

    ans = []
    for l in range(N):
        if seen[l]:
            ans.append(l+1)
    
    for t in ans:
        print(t)

main()
