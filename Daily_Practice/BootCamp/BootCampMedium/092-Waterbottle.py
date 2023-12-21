from math import atan, degrees

def main():
    a, b, x = map(int, input().split())
    if x >= a**2*b/2:
        print(degrees(atan(a/(2*b-2*x/a**2))))
    else:print(degrees(atan(2*x/a*b**2)))

main()