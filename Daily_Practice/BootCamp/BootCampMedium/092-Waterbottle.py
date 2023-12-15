from math import atan, degrees

def main():
    a, b, x = map(int, input().split())

    h = x / (a*a)
    res = b-h
    
    ans = degrees(atan(a/(b-h+res)))
    print(ans)

main()