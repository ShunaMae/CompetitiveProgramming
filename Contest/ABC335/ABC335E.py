def dfs(graph, A, v, last, memo):
    if v == len(A) - 1:
        return 1 if last <= A[v] else 0

    if (v, last) in memo:
        return memo[(v, last)]

    max_score = 0 if last > A[v] else 1
    for u in graph[v]:
        score = dfs(graph, A, u, max(A[v], last), memo)
        max_score = max(max_score, score + (last <= A[v]))

    memo[(v, last)] = max_score
    return max_score

def max_score_path(N, edges, A):
    graph = {i: [] for i in range(N)}
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    memo = {}
    return dfs(graph, A, 0, float('-inf'), memo)


N, M = map(int, input().split())
A = list(map(int, input().split()))
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

print(max_score_path(N, edges, A))
