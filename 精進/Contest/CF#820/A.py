for _ in range(int(input())):
    a, b, c = map(int, input().split())
    time_b = abs(b-c) + c 
    
    if a == time_b:
        print(3)
    elif a < time_b:
        print(1)
    else:
        print(2)