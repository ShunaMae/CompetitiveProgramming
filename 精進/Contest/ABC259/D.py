from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd, log2, log10, sqrt
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")

# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 9 + 1 

def judge(x1, y1, r1, x2, y2, r2):
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if (abs(r1 - r2)) ** 2 <= dist <= ((r1 + r2)**2):
        return True
    else:
        return False 

def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        circles.append([x, y, r])
    
    graph = [[] for _ in range(N+1)]
    for one in range(N):
        for two in range(one+1, N):
            x1, y1, r1 = circles[one][0], circles[one][1], circles[one][2]
            x2, y2, r2 = circles[two][0], circles[two][1], circles[two][2]
            if judge(x1, y1, r1, x2, y2, r2):
                graph[one].append(two)
                graph[two].append(one)
    
    stack = deque()
    # S
    s_grp = 0
    for i in range(N):
        if (sx - circles[i][0]) ** 2 + (sy - circles[i][1]) ** 2 == circles[i][2] ** 2:
            s_grp = i
            break 
    # t
    t_grp = 0
    for i in range(N):
        if (tx - circles[i][0]) ** 2 + (ty - circles[i][1]) ** 2 == circles[i][2] ** 2:
            t_grp = i
            break 
    
    seen = [(False) for _ in range(N+1)]
    seen[s_grp] = True
    stack.append(s_grp)
    while len(stack) > 0:
        to_check = stack.popleft()
        nxt = graph[to_check]
        for c in nxt:
            if not seen[c]:
                stack.append(c)
                seen[c] = True
            else:
                continue
    
    return seen[t_grp]

printout(main())

        