def ismap(): return map(int, input().split())
from collections import deque
import itertools
import operator

def monotone_increasing(lst):
    pairs = zip(lst, lst[1:])
    return all(itertools.starmap(operator.le, pairs))

def monotone_decreasing(lst):
    pairs = zip(lst, lst[1:])
    return all(itertools.starmap(operator.ge, pairs))

def monotone(lst):
    return monotone_increasing(lst) or monotone_decreasing(lst)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ismap())
        m = max(a)
        ind = a.index(m)
        first = monotone_increasing(a[:ind+1])
        second = monotone_decreasing(a[ind:])
        ans = first and second 
        if ans:
            print("YES")
        else:
            print("NO")
    
    return 
main()