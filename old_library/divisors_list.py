

def enum_divisors(n):
    """約数列挙 O(√N)"""

    divs_smaller = []
    divs_larger = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs_smaller.append(i)
            divs_larger.append(n // i)
        i += 1

    if divs_smaller[-1] == divs_larger[-1]:
        divs_smaller.pop()

    divisors = divs_smaller + divs_larger[::-1]

    return divisors


n = int(input())
print(enum_divisors(n))
# input: 100 
# [1, 2, 4, 5, 10, 20, 25, 50, 100]