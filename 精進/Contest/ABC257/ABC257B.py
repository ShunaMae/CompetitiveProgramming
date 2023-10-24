

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)
    L = list(map(int, input().split()))
    dp = [False] * N
    for i in A:
        dp[i-1] = True
    m = max(A)
    for op in L:
        if A[op-1] == N:
            continue 
        else:
            if dp[A[op-1]]:
                continue 
            else:
                dp[A[op-1]-1] = False
                dp[A[op-1]] = True
                A[op-1] += 1
                A = sorted(A)
        #print(dp, A)
        
    
    print(*A)

main()


