N, X = map(int, input().split())
li = []

for i in range(65, 91):
    for j in range(N):
        li.append(chr(i))

# print(li)
print(li[X-1])