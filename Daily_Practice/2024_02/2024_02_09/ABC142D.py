from math import gcd 

A, B = map(int, input().split())
a = gcd(A, B)

# [[factor, time]]
def factorize(N) -> list:
    ans = []

    for p in range(2, N):
        # while p * p <= N
        if p * p > N:
            break 

        # if N cannot be divided by p
        # skip p
        if N % p != 0:
            continue 

        # power 
        e = 0
        while N % p == 0:
            e += 1
            N //= p

        ans.append([p, e])
    
    if N != 1:
        ans.append([N, 1])
    
    return ans 

ans = factorize(a)
print(len(ans)+1)
