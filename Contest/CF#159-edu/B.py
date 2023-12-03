## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]


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
from math import gcd, log2, log10, ceil
from functools import lru_cache

def main():
    n, p, l, t = is_map(int)
    num_of_practicals = ceil(n/7)
    max_point = l + 2 * t
    num_lessons_attended = 0

    while True:

        if num_of_practicals <= 1:
            break 
        if p <= 0:
            break 

        p -= max_point
        num_of_practicals -= 2
        num_lessons_attended += 1
    
    while True:

        if p > 0:
            if num_of_practicals == 0:
                num_lessons_attended += ceil(p/l)
                break
            elif num_of_practicals == 1:
                p -= (l+t)
                num_of_practicals = 0
                num_lessons_attended += 1
        
        if p <= 0:
            break 
    
    print(n-num_lessons_attended)

# for _ in range(is_int()):
#     main()

def solve():
    n, p, l, t = is_map(int)
    num_of_practicals = ceil(n/7)
    num_days = 0

    # print(num_of_practicals)

    for i in range(1, num_of_practicals, 2):
        p -= (2*t+l)
        num_days += 1
        if p <= 0:
            return n-num_days
    
    p -= (t+l)
    if p <= 0:
        return n-num_days-1
    
    num_days += 1

    return n-num_days-ceil(p/l)
    
    
for _ in range(is_int()):
    print(solve())




















#     total_points_for_tasks = num_of_practicals * t
#     num_lessons_attended = ceil(num_of_practicals/2)
#     lesson_point = num_lessons_attended * l

# # if p < total_points_for_tasks:



#     p -= (total_points_for_tasks + lesson_point)

#     print(total_points_for_tasks, lesson_point)
#     if p <= 0:
#         print(n-num_lessons_attended)
#     else:
#         additional_days = ceil(p/l)
#         print(num_lessons_attended, additional_days)
#         print(n-num_lessons_attended-additional_days)




