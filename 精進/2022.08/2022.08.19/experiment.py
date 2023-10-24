
import sys
input = sys.stdin.readline
def main():
    n, m = [*map(int, input().strip().split())]
    a = [*map(int, input().strip().split())]
    sem, prev = 1, 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            prev += 1
            sem += prev
        else:
            prev += 1 + i
            sem += prev
    for i in range(m):
        x, y = [*map(int, input().strip().split())]
        x -= 1
        if a[x] == y:
            print(sem)
            continue
        if x - 1 >= 0:
            if a[x - 1] == a[x]:
                sem += x * (n - x)
            if a[x - 1] != a[x] and a[x - 1] == y:
                sem -= x * (n - x)
        if x + 1 <= n - 1:
            if a[x] == a[x + 1]:
                sem += (x + 1) * (n - x - 1)
            if a[x] != a[x + 1] and a[x + 1] == y:
                sem -= (x + 1) * (n - x - 1)
        a[x] = y
        print(sem)
 
 
for _ in range(1):
    main()