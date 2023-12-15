from collections import Counter

def main():
    n = int(input())
    v = list(map(int, input().split()))

    even = []
    odd = []
    for i in range(n):
        if i%2:
            even.append(v[i])
        else:
            odd.append(v[i])
    
    ec = Counter(even).most_common()
    oc = Counter(odd).most_common()
    cnt = 0

    if len(ec) == 1 and len(oc) == 1:
        if ec[0][0] == oc[0][0]:
            cnt += ec[0][1]
    elif len(ec) == 1:
        if oc[0][0] == ec[0][0]:
            cnt += len(odd)-oc[1][1]
        else:
            cnt += len(odd)-oc[0][1]
    elif len(oc) == 1:
        if oc[0][0] == ec[0][0]:
            cnt += len(even)-ec[1][1]
        else:
            cnt += len(even)-ec[0][1]
    else:
        if oc[0][0] == ec[0][0] and oc[0][1] > ec[0][1]:
            cnt += len(even)-ec[1][1]
            cnt += len(odd)-oc[0][1]
        elif oc[0][0] == ec[0][0] and oc[0][1] <= ec[0][1]:
            cnt += len(even)-ec[0][1]
            cnt += len(odd)-oc[1][1]    
        else:
            cnt += len(even)-ec[0][1]
            cnt += len(odd)-oc[0][1]
    
    print(cnt)

main()
                


