N = int(input())

left = []
right = []

for _ in range(N):
    num, hand = map(str, input().split())
    if hand == "L":
        left.append(int(num))
    else:
        right.append(int(num))

ans = 0

if len(left) > 0:
    left_start = left[0]
    for nxt in left:
        ans += abs(nxt-left_start)
        left_start = nxt 
if len(right) > 0:
    right_start = right[0]
    for nxt1 in right:
        ans += abs(nxt1-right_start)
        right_start = nxt1

print(ans)