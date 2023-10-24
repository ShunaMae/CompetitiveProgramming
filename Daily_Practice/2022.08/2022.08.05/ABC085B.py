def isint(): return int(input())

def main():
    N = isint()
    A = []
    for _ in range(N):
        s = isint()
        A.append(s)
    A = sorted(A)
    ans = 0

    for i in range(N):
        if i == 0:
            ans += 1 
            last = A[i]
        else:
            if A[i] > last:
                ans += 1 
                last = A[i]
            else:
                continue 
    
    return ans 

print(main())
            

