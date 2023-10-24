from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr, deg2rad
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd, log2, log10, sin, cos, atan, pi


# from numpy import deg2rad
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

a, b, d = map(int, input().split())
# theta = atan(b / a) * 180 / pi
# new_theta = (theta + d) * pi / 180
# x = sin(new_theta) / sin(atan(b / a)) * a
# y = cos(new_theta) / cos(atan(b / a)) * b
# print(x, y)
theta = d * pi / 180
x = a * cos(theta) - b * sin(theta)
y = a * sin(theta) + b * cos(theta)
print(x, y)