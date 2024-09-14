from itertools import combinations 
from copy import deepcopy
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

if N > 8:
    N = 8
    N = N[:8]

d  = defaultdict(list)



