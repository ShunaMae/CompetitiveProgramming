def primes_boolean(n):
    is_prime = ([False, True] * (n//2+1))[0: n+1]
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, n+1, 2):
        if not(is_prime[i]):
            continue
        if i*i > n:
            break
        for k in range(i*i, n+1, i):
            is_prime[k] = False
    return is_prime

n = int(input())
print(primes_boolean(n))


# input : 10
# 10
# [False, False, True, True, False, True, False, True, False, False, False]