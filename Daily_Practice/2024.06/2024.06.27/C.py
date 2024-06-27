def solve(N, P):
    # print(P)
    current = N
    generations = 0
    while current != 1:
        current = P[current]
        generations += 1
    
    return generations

N = int(input())
li = list(map(int, input().split()))
P  = [0, 0]
for i in li:
    P.append(i)
ans = solve(N, P)
print(ans)
