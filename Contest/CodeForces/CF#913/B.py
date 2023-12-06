from collections import deque

def main():
    s = list(input()) 

    upper_letter = deque([])
    lower_letter = deque([])

    for i in range(len(s)):
        # print(upper_letter)
        # print(lower_letter)
        if s[i] == "b" and len(lower_letter) > 0:
            lower_letter.pop()
        elif s[i] == "B" and len(upper_letter) > 0:
            upper_letter.pop()
        elif s[i] == "b" or s[i] == "B":
            continue
        elif s[i].isupper():
            upper_letter.append([i, s[i]])
        elif s[i].islower():
            lower_letter.append([i, s[i]])
        else:
            continue
    
    ans_list = sorted(lower_letter + upper_letter)

    ans = []
    for key in ans_list:
        _, l = key
        ans.append(l)
    
    print("".join(ans))

for _ in range(int(input())):
    main()


