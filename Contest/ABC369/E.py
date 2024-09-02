import heapq
from collections import defaultdict

INF = float('inf')

def dijkstra(N, graph, start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, time in graph[u]:
            if dist[u] + time < dist[v]:
                dist[v] = dist[u] + time
                heapq.heappush(pq, (dist[v], v))
    
    return dist[end]

def main():
    N, M = map(int, input().split())
    
    bridges = []
    
    for _ in range(M):
        Ui, Vi, Ti = map(int, input().split())
        bridges.append((Ui, Vi, Ti))
    
    Q = int(input())
    
    results = []
    
    for _ in range(Q):
        K = int(input())
        selected_bridges = list(map(int, input().split()))
        
        total_time = 0
        start_island = 1
        
        for j in selected_bridges:
            U, V, T = bridges[j-1]
            subgraph = defaultdict(list)
            subgraph[U].append((V, T))
            subgraph[V].append((U, T))
            
            time_to_bridge = dijkstra(N, subgraph, start_island, U)
            if time_to_bridge == INF:
                total_time = -1
                break
            total_time += time_to_bridge + T
            start_island = V  
    
        if total_time != -1:
            time_to_end = dijkstra(N, subgraph, start_island, N)
            if time_to_end == INF:
                total_time = -1
            else:
                total_time += time_to_end
        
        results.append(total_time)
    
    for result in results:
        print(result)

main()