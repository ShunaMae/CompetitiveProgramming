t = int(input())


def main():
    N, M = map(int, input().split())
    s = list(input())
    ind = list(map(int, input().split()))
    c = list(input())

    sorted_ind = sorted(ind)
    sorted_c = sorted(c)

    for i in range(M-1):
        cur = sorted_ind[i]
        nex = sorted_ind[i+1]
        if cur == nex:
            del sorted_c[-1]
    
    ind_set = sorted(list(set(ind)))

    # print(ind_set)
    # print(sorted_c)

    for j in range(len(ind_set)):
        s[ind_set[j]-1] = sorted_c[j]
    
    print("".join(s))


for _ in range(t):
    main()

        

