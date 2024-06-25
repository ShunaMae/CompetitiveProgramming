t = int(input())

for _ in range(t):
    a = sorted(list(map(int, input().split())))
    print((a[2]-a[1]) + (a[1]-a[0]))

