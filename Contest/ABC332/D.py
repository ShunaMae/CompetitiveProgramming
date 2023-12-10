from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, chain
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache

def move_row(matrix, row_index, new_index):
    # Pop the specified row
    moved_row = matrix.pop(row_index)
    # Insert it at the new index
    matrix.insert(new_index, moved_row)

def move_col(matrix, col_index, new_index):
    # Pop the specified column
    moved_column = [row.pop(col_index) for row in matrix]
    # Insert it at the new index in each row
    for i in range(len(matrix)):
        matrix[i].insert(new_index, moved_column[i])

def main():
    H,W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]

    A_flat = sorted(list(chain.from_iterable(A)))
    B_flat = sorted(list(chain.from_iterable(B)))
    if A_flat != B_flat:
        return -1 
    elif A == B:
        return 0
    
    cnt = 0
    for row in range(H-1):
        for col in range(W-1):
            if A[row][col] == B[row][col]:
                continue
            #print(row, col)
            dist_list = []
            for r in range(H):
                for c in range(W):
                    if r <= row and c <= col:
                        continue
                    if A[row][col] == B[r][c]:
                        dist_list.append([(abs(row-r)+abs(col-c)), r, c])
            #print(dist_list)
            dist_list = sorted(dist_list)
            if row != dist_list[0][1]:
                move_row(A, row, dist_list[0][1])
            if col != dist_list[0][2]:
                move_col(A, col, dist_list[0][2])
            cnt += dist_list[0][0]

            # print(A)

            if A == B:
                return cnt 
    
    if A != B:
        return -1 
    
def rotate_2d_list(input_list):
    # Use zip to transpose the list
    transposed = list(zip(*input_list))
    
    # If you want a list of lists instead of tuples
    rotated_list = [list(row) for row in transposed]
    
    return rotated_list

def solve():
    H,W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]

    A_flat = sorted(list(chain.from_iterable(A)))
    B_flat = sorted(list(chain.from_iterable(B)))
    if A_flat != B_flat:
        return -1 
    elif A == B:
        return 0
    
    cnt = 0

    for row in range(H):
        if sorted(A[row]) != sorted(B[row]):
            return -1
        for col in range(W):
            if A[row][col] == B[row][col]:
                continue
            print(row, col)
            indices = [i for i, x in enumerate(A[row]) if x == B[row][col] and i > col]
        
            cnt += (indices[0]-col)
            A[row][col], A[row][indices[0]] = A[row][indices[0]], A[row][col]
            if A[row] == B[row]:
                continue
    
    print(A)
    print("Hello")
    A_zip = rotate_2d_list(A)
    B_zip = rotate_2d_list(B)

    for row in range(H):
        if sorted(A_zip[row]) != sorted(B_zip[row]):
            return -1
        for col in range(W):
            if A_zip[row][col] == B_zip[row][col]:
                continue
            print(row, col)
            indices = [i for i, x in enumerate(A_zip[row]) if x == B_zip[row][col] and i > col]
            cnt += (indices[0]-col)
            A_zip[row][col], A_zip[row][indices[0]] = A_zip[row][indices[0]], A_zip[row][col]
            if A_zip[row] == B_zip[row]:
                break 
    
    print("Hi")
    print(A_zip)
    print(cnt)


solve()


            





