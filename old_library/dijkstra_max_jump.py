# dijikstra that computes max jumps 
# can recreate the path after distance is clarified 


from string import ascii_lowercase
li = list(ascii_lowercase)

import heapq 

def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s, 0) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]

class PriorityQueue:
    def __init__(self):
        self._container = []

    def push(self, x):
        heapq.heappush(self._container, x)

    def pop(self):
        return heapq.heappop(self._container)

    def __len__(self):
        return len(self._container)



INF = 10 ** 18 + 1

def dijkstra(s, N, graph):
    # shorted distance from the start 
    # [distance, jumps, prev_v]
    dist = [[INF, 0, -1] for _ in range(N)]
    # start
    dist[s][0] = 0
    seen = isseen(N)
    heap_q = PriorityQueue() # (distance, node, jumps)
    heap_q.push((0, s, 0))

    while heap_q:
        # first just needed for heap to sort the nodes 
        # nodes (v) is needed to record the vectors 
        # 
        _ , v, jump = heap_q.pop()
        seen[v] = True 
        for adjacent_node in graph[v]:
            v2, cost = adjacent_node[0], adjacent_node[1]
            if not seen[v2] \
                and dist[v][0] + cost <= dist[v2][0]:
                # if all and all
                    # update the cost 
                    dist[v2][0] = dist[v][0] + cost 
                    # jump
                    dist[v2][1] = jump + 1 
                    # prev vector 
                    dist[v2][2] = v
                    heap_q.push((dist[v2][0], v2, dist[v2][1]))
    
    return dist 

def get_path(t, dist):
    path = []
    while t != -1:
        path.append(t)
        t = dist[t][2]
    path.reverse()
    return path


# s = list(input())
# for i in range(len(s)):
#     s[i] = li.index(s[i]) + 1
# # print(s)
# graph = [[] for _ in range(len(s))]
# for j in range(len(s)):
#     for k in range(len(s)):
#         if k != j:
#             graph[j].append([k, abs(s[j] - s[k])])
# # print(graph)
# d = dijkstra(0, len(s), graph)
# longest_path = get_path(len(s)-1, d)
# print(d[-1][0], d[-1][1] + 1)
# print(*list(map(lambda x: x+1, longest_path)))

for _ in range(int(input())):
    s = list(input())
    for i in range(len(s)):
        s[i] = li.index(s[i]) + 1
    # print(s)
    graph = [[] for _ in range(len(s))]
    for j in range(len(s)):
        for k in range(len(s)):
            if k != j:
                graph[j].append([k, abs(s[j] - s[k])])
    # print(graph)
    d = dijkstra(0, len(s), graph)
    longest_path = get_path(len(s)-1, d)
    print(d[-1][0], d[-1][1] + 1)
    print(*list(map(lambda x: x+1, longest_path)))



