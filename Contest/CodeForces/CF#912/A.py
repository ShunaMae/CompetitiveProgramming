from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    max_period = 0

    idx = 0
    period = 1
    while True:

        if idx >= n-1:
            break 
        
        if a[idx] <= a[idx+1]:
            max_period = max(max_period, period)
            period = 0
        else:
            period += 1
            max_period = max(max_period, period)
            
        
        idx += 1
    
    # print(max_period)
    if max_period <= k:
        print("YES")
    else:
        print("NO")

# main()
for _ in range(int(input())):
    main()

