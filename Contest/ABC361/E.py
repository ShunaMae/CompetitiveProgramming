from typing import List, Tuple
import sys
sys.setrecursionlimit(10**6)

def dfs(graph: List[List[Tuple[int, int]]], v: int, visited: set, total_nodes: int, double_count_edges: set) -> int:
    """深さ優先探索（DFS）で全ての都市を訪れる経路を計算"""
    visited.add(v)
    total_distance = 0

    for u, length in graph[v]:
        if u not in visited:
            total_distance += length
            total_distance += dfs(graph, u, visited, total_nodes, double_count_edges)
            if (v, u) in double_count_edges or (u, v) in double_count_edges:
                total_distance += length  # 帰り道も追加する

    return total_distance

def find_farthest_node(graph: List[List[Tuple[int, int]]], start: int) -> Tuple[int, int]:
    """与えられた開始点から最も遠いノードとその距離を返す"""
    n = len(graph)
    visited = [False] * n
    stack = [(start, 0)]
    farthest_node = start
    max_distance = 0

    while stack:
        node, distance = stack.pop()
        visited[node] = True

        if distance > max_distance:
            max_distance = distance
            farthest_node = node

        for neighbor, length in graph[node]:
            if not visited[neighbor]:
                stack.append((neighbor, distance + length))

    return farthest_node, max_distance

def find_path(graph: List[List[Tuple[int, int]]], start: int, end: int) -> List[int]:
    """与えられた開始点と終点間のパスを返す"""
    n = len(graph)
    parent = [-1] * n
    stack = [(start, -1)]

    while stack:
        node, par = stack.pop()
        parent[node] = par
        if node == end:
            break
        for neighbor, _ in graph[node]:
            if neighbor != par:
                stack.append((neighbor, node))

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

def find_tree_diameter(graph: List[List[Tuple[int, int]]]) -> Tuple[int, int, int]:
    """木の直径を見つけ、その両端のノードと直径の長さを返す"""
    # 任意のノードから開始して最も遠いノードを見つける
    start_node = 0
    farthest_node, _ = find_farthest_node(graph, start_node)
    # 見つかった最も遠いノードから再度最も遠いノードを見つける
    other_farthest_node, diameter = find_farthest_node(graph, farthest_node)

    return farthest_node, other_farthest_node, diameter

def main():
    # 入力データの読み込み
    N = int(input())
    edges = []

    for _ in range(N-1):
        a, b, c = map(int, input().split())
        edges.append((a-1, b-1, c))  # 0-indexed に変換

    # 隣接リストの構築
    graph = [[] for _ in range(N)]
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 木の直径を求め、その端点からDFSを行う
    start_node, end_node, _ = find_tree_diameter(graph)
    path = find_path(graph, start_node, end_node)

    # 木の直径に含まれる辺を求める
    diameter_edges = set()
    for i in range(len(path) - 1):
        diameter_edges.add((path[i], path[i+1]))
        diameter_edges.add((path[i+1], path[i]))

    visited = set()
    total_distance = dfs(graph, start_node, visited, N, diameter_edges)

    # 計算した距離を出力
    print(total_distance)

main()