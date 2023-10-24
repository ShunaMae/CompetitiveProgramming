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
    h1, w1 = ismap()
    field1 = []
    for _ in range(h1):
        s = list(ismap())
        field1.append(s)
    h2, w2 = ismap()
    field2 = []
    for _ in range(h2):
        s = list(ismap())
        field2.append(s)
    
    start_r = -1
    start_c = -1
    for r in range(h1 - h2 + 1):
        for c in range(w1 - w2 + 1):
            if field1[r][c] == field2[0][0]:
                start_r = r 
                start_c = c 
    
    # print(start_r, start_c)

    if start_r == -1 or start_c == -1:
        return False
    if h2 == 1 and w2 == 1:
        return True
        

    a = 0
    field3 = []
    field3.append(field1[start_r][start_c:])
    now = field2[a][0]
    for r in range(h1):   
        if r < start_r:
            continue 
        elif r == start_r:
            a += 1 
            now = field2[a][0]
        else:
            if field1[r][start_c] == now:
                if a < (h2 - 1):
                    field3.append(field1[r][start_c:])
                    a += 1
                    now = field2[a][0]
                elif a == (h2-1):
                    field3.append(field1[r][start_c:])
                    break 
                else:
                    break 
            else:
                continue 
    if a != (h2-1):
        return False 
    # for i in range(len(field3)):
    #     print(field3[i])
    field3 = list(map(list, zip(*field3)))
    field_2_new = list(map(list, zip(*field2)))

    # for i in range(len(field3)):
    #     print(field3[i])
    # for j in range(len(field_2_new)):
    #     print(field_2_new[j])

    field4 = []
    field4.append(field3[0])
    b = 0 
    now = field_2_new[1][0]
    # print(now, "now")
    for r in range(w1 - start_c):
        if r < start_c:
            continue 
        if r == start_c:
            b += 1
            now = field_2_new[b][0]
        else:
            if field3[r][0] == now:
                if b < (w2-1):
                    field4.append(field3[r])
                    b += 1
                    now = field_2_new[b][0]
                    # print(now, b, "loop")
                elif b == (w2-1):
                    field4.append(field3[r])
                    break
                else:
                    break
            else:
                continue 
    # for i in range(len(field4)):
    #     print(field4[i])
    # print(now, b)
    if b != (w2-1):
        return False 
    

    
    field4 =  list(map(list, zip(*field4)))
    for r in range(h2):
        for c in range(w2):
            if field4[r][c] != field2[r][c]:
                return False 
    

    return True 

out(main())




    
    
    



                

        

