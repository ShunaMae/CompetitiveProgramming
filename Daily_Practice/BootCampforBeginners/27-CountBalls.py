
def main():
    N, A, B = map(int, input().split())
    ans = (N // (A+B)) * A
    ans += min(N%(A+B), A)
    print(ans)
main()