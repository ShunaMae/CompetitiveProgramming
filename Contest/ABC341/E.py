class LazySegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = [0] * (4 * self.n)  # Max size with padding for tree
        self.lazy = [0] * (4 * self.n)  # Lazy propagation storage
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, v, tl, tr):
        if tl == tr:
            self.data[v] = data[tl]
        else:
            tm = (tl + tr) // 2
            self.build(data, v*2, tl, tm)
            self.build(data, v*2+1, tm+1, tr)
            self.data[v] = self.data[v*2] + self.data[v*2+1]

    def push(self, v, tl, tr):
        if self.lazy[v]:
            self.data[v] = (tr-tl+1) - self.data[v]  # Flip the count of 1s to 0s and vice versa
            if tl != tr:  # Not a leaf
                self.lazy[v*2] ^= 1
                self.lazy[v*2+1] ^= 1
            self.lazy[v] = 0

    def update_range(self, v, tl, tr, l, r):
        self.push(v, tl, tr)
        if l > r:
            return
        if l == tl and r == tr:
            self.lazy[v] ^= 1
            self.push(v, tl, tr)
        else:
            tm = (tl + tr) // 2
            self.update_range(v*2, tl, tm, l, min(r, tm))
            self.update_range(v*2+1, tm+1, tr, max(l, tm+1), r)
            self.data[v] = self.data[v*2] + self.data[v*2+1]

    def query_range(self, v, tl, tr, l, r):
        if l > r:
            return 0
        self.push(v, tl, tr)
        if l == tl and r == tr:
            return self.data[v]
        tm = (tl + tr) // 2
        return self.query_range(v*2, tl, tm, l, min(r, tm)) + self.query_range(v*2+1, tm+1, tr, max(l, tm+1), r)

N, Q = map(int, input().split())
S = list(input())
data = [int(c) for c in S]  # Initial data array
lst = LazySegmentTree(data)

# Process queries
for _ in range(Q):
    t, l, r = map(int, input().split())
    l -= 1  # Adjust for 0-based indexing
    r -= 1  # Adjust for 0-based indexing
    if t == 1:
        lst.update_range(1, 0, lst.n - 1, l, r)
    else:
        ones = lst.query_range(1, 0, lst.n - 1, l, r)
        length = r - l + 1
        good_string = ones == 0 or ones == length or ones == 1 if l == r else ones * 2 == length
        print("Yes" if good_string else "No")
