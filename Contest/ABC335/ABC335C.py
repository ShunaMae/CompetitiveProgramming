N, Q = map(int, input().split())

point = [(i, 0) for i in range(N, 0, -1)]

for _ in range(Q):
    t, c = map(str, input().split())
    if t == "1":
        x,y = point[-1]
        if c == "U":
            y += 1
        elif c == "D":
            y -= 1
        elif c == "L":
            x -= 1
        else:
            x += 1
        point.append((x, y))
    else:
        print(*point[-int(c)])
    
