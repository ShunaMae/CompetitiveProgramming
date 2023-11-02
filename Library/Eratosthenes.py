
# judge if i is prime for all integer i between 1 and N
# returns a boolean list of [0, N+1] with prime number being True

def Eratosthenes(N: int) -> list:
    isprime = [True] * (N+1)
    # 0 and 1 are not prime numbers 
    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        # if its already a composite number, skip
        if not isprime[p]: continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p
        
    return isprime