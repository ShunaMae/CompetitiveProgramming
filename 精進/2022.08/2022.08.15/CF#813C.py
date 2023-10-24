def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m_inc = []
    bad_indices = set()
    for i in range(n):
        if a[i] in bad_indices:
            a[i] = 0
        if m_inc and a[i] < m_inc[-1]:
            bad_indices.update(m_inc)
            m_inc = []
        m_inc.append(a[i])
    bad_indices.add(0)
    return len(bad_indices) - 1

for _ in range(int(input())):
    print(solve())
    