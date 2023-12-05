
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    n, x = is_map(int)
    a = list(is_map(int))
    dist_list = []
    for i in range(n):
        if i == 0:
            dist_list.append(a[0])
        else:
            dist_list.append(a[i]-a[i-1])
    dist_list.append((x-a[n-1])*2)
    # print(dist_list)
    print(max(dist_list))

for _ in range(is_int()):
    main()