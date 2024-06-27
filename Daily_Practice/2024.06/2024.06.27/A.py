N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict 
d = defaultdict(int)

for i in A:
    d[i] += 1

print(d)
for key, value in d.items():
    if value != 4:
        print(key)
        break 
