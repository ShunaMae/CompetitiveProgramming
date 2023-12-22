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
    cnt = 19**18

    if len(ec) == len(oc) == 1:
        cnt = 0
    elif ec[0][1] == oc[0][1]:
        cnt = min(len(ec)-ec[0][1]+len(oc)-oc[1][1], len(ec)-ec[1][1]+len(oc)-oc[0][1])
    else:
        cnt = len(ec)+len(oc)+ec[0][1]-oc[0][1]
    
    print(cnt)

main()



                


