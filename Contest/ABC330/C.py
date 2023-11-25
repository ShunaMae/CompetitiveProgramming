
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 
import bisect 

class SquareRoot(object):
    def __init__(self, n):
        self.n = n
    def __getitem__(self, index):
        return index * index
    def __len__(self):
        return self.n

def try_square_root(n2):
    n = bisect.bisect_left(SquareRoot(n2), n2)
    return n if n*n == n2 else None

def main():
    D = is_int()
    if try_square_root(D) != None:
        return 0
    
    for i in reversed(range(int(D**0.5)+1)):
        y_squared = D-i**2
        if try_square_root(y_squared) != None:
            return abs(i**2+y_squared-D)

print(main())


