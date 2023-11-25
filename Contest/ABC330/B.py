
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    N, L, R = is_map(int)
    A = list(is_map(int))
    ans = []
    for i in range(N):
        if A[i] <= L:
            ans.append(L)
        elif A[i] >= R:
            ans.append(R)
        else:
            ans.append(A[i])
    
    print(*ans)

main()
