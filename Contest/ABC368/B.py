import heapq

def solve(A):
    A = [-a for a in A]
    heapq.heapify(A)
    count = 0

    while len(A) > 1:
        max1 = -heapq.heappop(A)
        max2 = -heapq.heappop(A)

        max1 -= 1
        max2 -= 1

        if max1 > 0:
            heapq.heappush(A, -max1)
        if max2 > 0:
            heapq.heappush(A, -max2)

        count += 1

    return count

N = int(input())
A = list(map(int, input().split()))

print(solve(A))