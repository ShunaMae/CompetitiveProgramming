


def solve():
    s = list(input())
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    r = 8 - int(s[1])
    c = li.index(s[0])

    p = set()

    for row in range(8):
        for col in range(8):
            # print(row, col)
            if r == row and c == col:
                continue
            elif r == row or c == col:
                ans = li[col] + str(8 - row)
                p.add(ans)
    
    for i in p:
        print(i)

for _ in range(int(input())):
    solve()



