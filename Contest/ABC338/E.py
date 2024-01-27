from sortedcontainers import SortedSet
from bisect import bisect_right, bisect_left 

N = int(input())

events = []
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    events.append((a, 'start', b))
    events.append((b, 'end', a))
events.sort()

flag = False
S = SortedSet()
for point, kind, other_end in events:
    if kind == "start":
        index = S.bisect_right(other_end)
        if index != 0:
            flag = True
        S.add(other_end)
    else:
        S.discard(point)

if flag:
    print("Yes")
else:
    print("No")


