from re import L


def main():
    N, C = map(int, input().split())
    X = C
    for i in range(N):
        t, a = map(int, input().split())
        if t == 1:
            X ^= a
        elif t == 2:
            X &= a
        else:
            X |= a
    
    return 

A = 100

for i in range(30):
    A ^= 7
    print(A)
    A &= 7
    print(A)
    A |= 7
    print(A)
