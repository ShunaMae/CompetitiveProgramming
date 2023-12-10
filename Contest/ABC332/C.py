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



def split_list_by_zero(input_list):
    result = []
    sublist = []

    for value in input_list:
        if value == "0":
            if sublist:  # Check if the sublist is not empty
                result.append(sublist)
                sublist = []  # Reset the sublist
        else:
            sublist.append(value)

    if sublist:  # Append the last sublist if not empty
        result.append(sublist)

    return result

def main():
    N, M = map(int, input().split())
    S = list(input())
    li = split_list_by_zero(S)
    ans = 0

    for i in li:
        one = i.count("1")
        two = i.count("2")

        one_needs = max(one-M, 0)
        needs = two+one_needs
        ans = max(ans, needs)
    
    print(ans)

main()






