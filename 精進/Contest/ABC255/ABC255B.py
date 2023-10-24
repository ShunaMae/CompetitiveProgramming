def main():
    N, M = map(int, input().split())
    max_K = 0
    K = set(map(int, input().split()))
    # 一番近いA_kとの距離の最大値
    A = []
    lighter = []
    for i in range(1, N+1):
        x, y = map(int, input().split())
        if i in K:
            lighter.append([x,y])
        else:
            A.append([x, y])
    
    abs_dist = 0
    # print(lighter, "lighter")
    # print(A, "A")
    for dark in range(len(A)):
        dist = 1000000000000000000000000000000
        for d in range(M):
            dist = min(dist, ((lighter[d][0] - A[dark-1][0]) ** 2 + (lighter[d][1] - A[dark-1][1]) ** 2))
            # print("coor", lighter[d][0], A[dark-1][0], lighter[d][1], A[dark-1][1])
                # print(dist)
        abs_dist = max(abs_dist, dist)
    
    print(abs_dist ** (1/2))

main()


    

