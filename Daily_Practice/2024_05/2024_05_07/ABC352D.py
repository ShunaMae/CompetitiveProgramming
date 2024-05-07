from sortedcontainers import SortedSet

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    new_P = [(0) for _ in range(N)]

    if K == 1:
        return 0

    for i in range(N):
        new_P[P[i]-1] = i

    S = SortedSet([])
    for j in range(K):
        S.add(new_P[j])

    start_min = S.pop(0)
    start_max = S.pop()
    ans = abs(start_min-start_max)

    S.add(start_min)
    S.add(start_max)

    for i in range(1,N-K):

        S.discard(new_P[i-1])
        S.add(new_P[i+K-1])


        min_s = S.pop(0)
        max_s = S.pop()
        ans = min(ans, abs(max_s - min_s))

        S.add(min_s)
        S.add(max_s)

        S.discard(new_P[i])
        S.add(new_P[i+K])


    return ans

print(main())

