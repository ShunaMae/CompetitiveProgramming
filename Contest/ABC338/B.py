from collections import Counter 

S = input()
A = Counter(S).most_common()

max_count = A[0][1]
most_frequent = [element for element, count in A if count == max_count]

print(min(most_frequent))