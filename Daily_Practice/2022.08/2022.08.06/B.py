def ismap(): return map(int, input().split())
from collections import deque
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ismap())
        m = min(a) 
        b = [i-m for i in a] 
        b = deque(b)
        flag = True
        edge = 0
        while True:
            if sum(b) <= 0:
                break 
            if not flag:
                break 
            if b[0] == edge:
                b.popleft()
                edge += 1 
            elif b[-1] == edge:
                b.pop()
                edge += 1 
            else:
                flag = False 
        if flag:
            print("YES")
        else:
            print("NO")
    return 

main()

        
