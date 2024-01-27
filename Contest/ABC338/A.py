S = input()
flag = True
for i in range(len(S)):
    if i == 0:
        if S[i].islower():
            flag = False 
    else:
        if S[i].isupper():
            flag = False 

if flag:
    print("Yes")
else:
    print("No")