from collections import Counter 

def main(first_input, second_input):
    n = first_input
    _, s = zip(*Counter(list(second_input)).most_common())
    # print(s)
    cur = s[0]
    i = 1
    while True:
        if cur-s[i] > 0:
            cur -= s[i]
            i += 1
        elif cur-s[i] == 0:
            if i+1 < len(s):
                cur = s[i+1]
                i += 2
            else:
                cur = 0
                break 
        else:
            cur = s[i]-cur
            i += 1
        if i > len(s) -1:
            break
    
    return cur


def minimum_length(s):
    stack = []

    for char in s:
        if stack and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)

    return len(stack)


for _ in range(int(input())):
    n = int(input())
    t = input()
    ans = min(main(n, t), minimum_length(t))
    print(ans)