from bisect import bisect_right, bisect_left

def main():
    N = int(input())
    S = list(input())
    children = []
    adults = []
    W = list(map(int, input().split()))
    w = set(W)
    w.add(0)
    w.add(10**9+1)
    for i in range(N):
        if S[i] == '0':
            children.append(W[i])
        else:
            adults.append(W[i])
    
    children = sorted(children)
    adults = sorted(adults)
    missed = 10**7
    # print(children)
    # print(adults)
    # print(w)

    for weight in w:
        missed_kids = len(children) - bisect_left(children, weight)
        missed_adults = bisect_left(adults, weight)
        # print(weight, missed_kids, missed_adults)
        missed = min(missed, missed_kids + missed_adults)
    
    return N - missed

print(main())