A, B = map(int, input().split())

ans = 0
if A == B:
    ans = 1 
elif abs(A-B) % 2 == 0:
    ans = 3 
else:
    ans = 2 

print(ans)
