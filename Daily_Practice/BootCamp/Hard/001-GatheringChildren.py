def greedy(l):
    pos = [(1) for _ in range(len(l))]
    for i in range(100):
        for j in range(len(l)):
            pos[j] -= 1
            if l[j] == "L":
                pos[j] -= 1
                pos[j-1] += 1
            else:
                pos[j+1] += 1
        print(*pos)

S = list(input())
greedy(S)
