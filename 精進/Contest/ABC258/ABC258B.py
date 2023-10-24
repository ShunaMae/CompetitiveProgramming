from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")

N = int(input())
field = []
m = 0
pool = set()
for i in range(N):
    a = list(map(int, list(str(input())))) 
    m = max(m, max(a))
    field.append(a)
ans = set()
for row in range(N):
    for col in range(N):
        if field[row][col] == m:
            # 縦
            down = []
            up = []
            for i in range(N):
                down.append(str(field[(row+i)%N][col]))
                up.append(str(field[(row-i)%N][col]))
            #横
            right = []
            left = []
            for j in range(N):
                right.append(str(field[row][(col+j)%N]))
                left.append(str(field[row][(col-j)%N]))
            
            # 斜め
            to_left = []
            to_right = []
            for k in range(N):
                to_left.append(str(field[(row+k)%N][(col+k)%N]))
                to_right.append(str(field[(row-k)%N][(col-k)%N]))
            
            to_l = []
            to_r = []
            for k in range(N):
                to_l.append(str(field[(row+k)%N][(col-k)%N]))
                to_r.append(str(field[(row-k)%N][(col+k)%N]))

            
            down = int("".join(down))
            up = int("".join(up))
            right = int("".join(right))
            left = int("".join(left))
            to_left = int("".join(to_left))
            to_right = int("".join(to_right))
            to_r = int("".join(to_r))
            to_l = int("".join(to_l))
            ans.add(down)
            ans.add(up)
            ans.add(right)
            ans.add(left)
            ans.add(to_left)
            ans.add(to_right)
            ans.add(to_l)
            ans.add(to_r)

print(ans)
print(max(ans))

            

