N = int(input())
S = input()

s = -1
e = -1

for i in range(N):
    if S[i] == "|" and s != -1:
        e = i
    elif S[i] == "|":
        s = i

if "*" in S[s:e]:
    print("in")
else:
    print("out") 