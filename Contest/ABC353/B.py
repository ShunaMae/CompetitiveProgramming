N, K = map(int, input().split())
from collections import deque
A = deque(list(map(int, input().split())))

ans = 0
available_seats = K

for people in A:
    if people > available_seats:
        ans += 1
        available_seats = K
    available_seats -= people
    
if available_seats != K:
    ans += 1

print(ans)

