def main():
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    ans = 0
    left = []
    skip_first = []
    for i in range(0, K-1, 2):
        left.append(A[i+1]-A[i])
        if i+2 < K:
            skip_first.append(A[i+2]-A[i+1])
    
    # print(left)
    # print(skip_first)
    B = [sum(skip_first)]
    if K%2 == 0:
        print(sum(left))
    # elif K == 1:
    #     print(A[0])
    else:
        tmp = sum(skip_first)
        for j in range(1, K, 2):
            tmp = tmp - (A[j+1] - A[j])
            tmp += A[j] - A[j-1]
            B.append(tmp)

    
        if len(B) == 0:
            print(0)
        else:
            print(min(B))
            


main()
