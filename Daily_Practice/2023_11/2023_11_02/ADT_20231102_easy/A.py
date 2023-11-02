
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    S = list(input())
    if len(set(S)) == 1:
        print(1)
    elif len(set(S)) == 2:
        print(3)
    else:
        print(6)

main()