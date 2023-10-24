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

def main():
    N, Q = map(int, input().split())
    S = list(input()) * 2
    first = len(S)
    for _ in range(Q):
        num, x = map(int, input().split())
        if num == 1:
            first = (first - x) % len(S)
        else:
            print(S[(first+x-1) % len(S)])

main()
