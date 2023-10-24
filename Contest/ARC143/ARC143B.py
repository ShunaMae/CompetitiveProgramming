MOD = 998244353
from math import factorial
N = int(input())
rest = N * (N-1) 
rem = factorial(rest) 
rem *= factorial(N) 
rem *= 2
print(rem % MOD)