N, M, K = map(int, input().split())
from math import lcm, gcd

def check(x, r):
    n =  x // N + x // M - x // d
    if n >= r:
        return True
    return False

d = lcm(N, M)
a = d // N + d // M - 2
cycles, remainder = K // a, K % a
# print(cycles, remainder, a)
def meguru_bisect(l, r):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    l r は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(r - l) > 1):
        mid = (r + l) // 2
        if check(mid, remainder):
            r = mid
        else:
            l = mid
    return r

def kth_smallest(N, M, K):
    # If K is exactly at the end of a cycle
    if remainder == 0:
        return cycles * d - min(N, M)
    else:
        low, high = 0, d  # Upper bound for binary search
        return cycles * d + meguru_bisect(low, high)

print(kth_smallest(N, M, K))