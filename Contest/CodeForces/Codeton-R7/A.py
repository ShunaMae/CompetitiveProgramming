
def try_sorting(a, N):
    for i in range(1, N-1):
        if a[i-1] < a[i] and a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    for _ in range(100):
        a = try_sorting(a, n)
    
    if a == a_sorted:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    main()
