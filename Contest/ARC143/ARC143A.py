def main():
    A, B, C = map(int, input().split())
    cnt = 0
    li = sorted([A, B, C])
    m = min(li) 
    cnt += (li[1] - m)
    li[2] -= (li[1] - m)
    li[1] = m
    li.sort()
    # print(li)
    gap = li[2] - m
    if gap <= li[0]:
        cnt += gap 
        cnt += gap 
        cnt += (m - gap) 
        return cnt 
    else:
        return -1

print(main())