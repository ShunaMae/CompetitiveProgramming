from string import ascii_lowercase
from collections import deque 
li = list(ascii_lowercase)
for _ in range(int(input())):
    n = int(input())
    t = deque(reversed(list(input())))
    ans = ""
    # print(t)
    while len(t) != 0:
        if len(t) == 0:
            break
        num = int(t.popleft())
        if num == 0:
            temp = t.popleft()
            temp = t.popleft() + temp
            int_t = int(temp)
            ans += li[int_t-1]
            #print(ans)
            if len(t) == 0:
                break
        else:
            # print(t)
            # print(num, "num")
            ans += li[num-1]
            #print(ans)
            if len(t) == 0:
                break
        if len(t) == 0:
            break
    
    print("".join(reversed(list(ans))))





