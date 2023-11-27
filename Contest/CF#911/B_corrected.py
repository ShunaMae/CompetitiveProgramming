
def main():
    a, b, c = map(int, input().split())
    if len(set([a,b,c])) == 1:
        ans = [1,1,1]
    else:
        ans = []
        if abs(b-c)%2==0: ans.append(1)
        else: ans.append(0)

        if abs(a-c)%2==0: ans.append(1)
        else: ans.append(0)

        if abs(a-b)%2==0: ans.append(1)
        else: ans.append(0)
    
    print(*ans)

for _ in range(int(input())):
    main()