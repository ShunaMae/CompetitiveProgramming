d = ".jp"

s = reversed(list(input()))

ans = []
for i in s:
    if i == ".":
        break
    ans.append(i)

print("".join(reversed(ans)))