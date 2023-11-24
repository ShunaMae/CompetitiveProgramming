
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 
from collections import deque 

# 単調減少（同じも含む）している区間は最大値分テレポートすればよい
def main():
    n = is_int()
    c_tele = list(is_map(int))
    ans = c_tele[0]
    start = 0
    for end in range(n):
        if start == end:
            min_seq = c_tele[start]
        else:
            min_seq = c_tele[end-1]

        if min_seq < c_tele[end]:
            # 単調減少が崩れている
            # print(end)
            ans += (c_tele[end] - min_seq)
            start = end
    
    print(ans-1)

# main()

for _ in range(is_int()):
    main()


                





    