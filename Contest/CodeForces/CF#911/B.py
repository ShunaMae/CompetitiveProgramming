def greedy(a,b,c) -> list:

    cnt = 0

    while True:

        if a+b+c == 1:
            break 
        if cnt > 500:
            break 

        if min(a,b,c) == a and max(a,b,c) == c:
            a,b,c = a+b, b-b, c-b
        elif min(a,b,c) == a and max(a,b,c) == b:
            a,b,c = a+c, b-c, c-c
        elif min(a,b,c) == b and max(a,b,c) == a:
            a,b,c = a-c, b+c, c-c
        elif min(a,b,c) == b and max(a,b,c) == c:
            a,b,c = a-a, b+a, c-a
        elif min(a,b,c) == c and max(a,b,c) == a:
            a,b,c = a-b, b-b, c+b
        else: #min(a,b,c) == c and max(a,b,c) == b
            a,b,c = a-a, b-a, c+a

        print(a,b,c)
        cnt += 1
    
    value = [a,b,c]
    # for i in range(3):
    #     if value[i] != 0:
    #         value[i] = 1
    
    return value


        


def main():
    a, b, c = map(int, input().split())
    if len(set([a,b,c])) == 1:
        ans = [1,1,1]
    elif len(set([a,b,c])) == 2:
        if a==b:
            ans = [0,0,1]
        elif a==c:
            ans = [0,1,0]
        else:
            ans = [1,0,0]
    else:
        # ans = []
        # if abs(b-c)%2==0 and (a+min(b,c))>=(abs(b-c)//2): ans.append(1)
        # else: ans.append(0)

        # if abs(a-c)%2==0 and (b+min(a,c))>=(abs(a-c)//2): ans.append(1)
        # else: ans.append(0)

        # if abs(a-b)%2==0 and (c+min(a,b))>=(abs(a-b)//2): ans.append(1)
        # else: ans.append(0)

        ans = greedy(a,b,c)
    
    print(*ans)

# for _ in range(int(input())):
#     main()

print(greedy(98,100,2))