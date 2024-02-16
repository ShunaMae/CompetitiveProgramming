
from bisect import bisect_left

def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            # i+j=kでは直線になってしまう
            idx = bisect_left(L, L[i]+L[j])-1
            #ｊより小さい場合を削除
            if idx-j > 0:
                ans += idx-j
    
    print(ans)


main()