## Q1. マス目の経路最適化（１）

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    dp = [[(0) for _ in range(N)] for _ in range(3)]
    dp[0][0] = A[0]
    dp[0][1] = B[0]
    dp[0][2] = C[0]

    for grid in range(N):
        # (i, grid) から (j, grid+1) への遷移
        for i in range(3):
            for j in range(3):
                

        

