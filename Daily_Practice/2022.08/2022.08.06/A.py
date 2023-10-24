def ismap(): return map(int, input().split())

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        x_max = 0
        x_min = 0
        y_max = 0
        y_min = 0
        for _ in range(n):
            x, y = ismap()
            x_max = max(x_max, x)
            x_min = min(x_min, x)
            y_max = max(y_max, y)
            y_min = min(y_min, y)
        
        # print(x_max, x_min, y_max, y_min)
        if x_max <= 0:
            sx = abs(x_min) * 2 
        elif x_min >= 0:
            sx = abs(x_max) * 2 
        else:
            sx = (x_max + abs(x_min)) * 2 
        
        if y_max <= 0:
            sy = abs(y_min) * 2 
        elif y_min >= 0:
            sy = y_max * 2 
        else:
            sy = (abs(y_min) + y_max) * 2 
        print(sx + sy)
    
    return 

main()

