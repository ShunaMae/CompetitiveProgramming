
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    N, L = is_map(int)
    A = list(is_map(int))
    ans = 0
    for i in range(N):
        if A[i] >= L:
            ans += 1
    
    print(ans)

main()