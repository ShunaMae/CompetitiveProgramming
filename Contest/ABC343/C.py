from collections import defaultdict
N = int(input())

li = []
num = 1
while True:
    to_test = str(num**3)
    if num**3 > N:
        break 
    if to_test == to_test[::-1]:
        li.append(num**3)

    num += 1

print(max(li))

