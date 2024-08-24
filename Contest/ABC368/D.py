import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict

def dfs_lca(node, parent, depth):
    euler.append(node)
    depth_list[node] = depth
    first_occurrence[node] = len(euler) - 1

    for neighbor in tree[node]:
        if neighbor != parent:
            dfs_lca(neighbor, node, depth + 1)
            euler.append(node)

def build_sparse_table():
    m = len(euler)
    for i in range(m):
        sparse_table[0][i] = euler[i]

    j = 1
    while (1 << j) <= m:
        i = 0
        while (i + (1 << j) - 1) < m:
            if depth_list[sparse_table[j - 1][i]] < depth_list[sparse_table[j - 1][i + (1 << (j - 1))]]:
                sparse_table[j][i] = sparse_table[j - 1][i]
            else:
                sparse_table[j][i] = sparse_table[j - 1][i + (1 << (j - 1))]
            i += 1
        j += 1

def query_lca(u, v):
    left = first_occurrence[u]
    right = first_occurrence[v]
    if left > right:
        left, right = right, left

    j = log[right - left + 1]
    if depth_list[sparse_table[j][left]] < depth_list[sparse_table[j][right - (1 << j) + 1]]:
        return sparse_table[j][left]
    else:
        return sparse_table[j][right - (1 << j) + 1]

def dfs(node, parent):
    is_contained = node in special_vertices
    for neighbor in tree[node]:
        if neighbor != parent:
            if dfs(neighbor, node):
                is_contained = True
                result[0] += 1
    return is_contained

N, K = map(int, input().split())
tree = defaultdict(list)

for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

special_vertices = list(map(int, input().split()))

euler = []
depth_list = [0] * (N + 1)
first_occurrence = [-1] * (N + 1)
log = [0] * (2 * N)
sparse_table = [[0] * (2 * N) for _ in range(20)]

dfs_lca(1, -1, 0)

for i in range(2, 2 * N):
    log[i] = log[i // 2] + 1

build_sparse_table()

lca = special_vertices[0]
for i in range(1, K):
    lca = query_lca(lca, special_vertices[i])

result = [0]
dfs(lca, -1)

print(result[0] + 1)