import sys
input = sys.stdin.buffer.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = n + n * (n-1) // 2 

for j in range(1, n):
    if a[j] != a[j-1]:
        ans += j * (n-j)


for _ in range(m):
    i, q = map(int, input().split())
    i -= 1
    if q == a[i]:
        print(ans)
    else:
        if i > 0:
            if a[i-1] == a[i]:
                ans += i * (n-i)
            elif a[i-1] != a[i] and a[i-1] == q:
                ans -= i * (n-i)
        if i < n-1:
            if a[i+1] == a[i]:
                ans += (i+1) * (n-i-1)
            elif a[i+1] != a[i] and a[i+1] == q:
                ans -= (i+1) * (n-i-1)
        a[i] = q
        print(ans)

        


