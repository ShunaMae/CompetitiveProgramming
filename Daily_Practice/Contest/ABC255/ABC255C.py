def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        return abs(X - A)
    else:
        An = (N-1)*D + A
        if min(A, An) > X:
            return abs(min(A, An) - X)
        elif max(A, An) < X:
            return abs(max(A, An) - X)
        else:
            term = abs((X-A) // D) + 1
            # print(term, "first")
            diff = 100000000000000000000
            seq = []
            # print(term, "second")
            for i in range(term-2, term+2):
                seq.append((i * D) + A)
            # print(seq)
            for terms in range(len(seq)):
                diff = min(diff, abs(seq[terms] - X))
                # print(diff, terms, "this is")
            return diff 

print(main())



