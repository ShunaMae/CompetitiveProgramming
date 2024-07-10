from collections import deque
from copy import deepcopy

def bfs(N, S, T):
    initial_state = list(S) + ['.', '.']
    goal_state = list(T) + ['.', '.']
    queue = deque([(initial_state, 0)])
    visited = set()
    visited.add(tuple(initial_state))

    while queue:
        current, moves = queue.popleft()
        
        # # デバッグ: 現在の状態と移動回数を表示
        # print(f"Current state: {current}, Moves: {moves}")

        if current[:N] == goal_state[:N]:
            return moves
        
        for i in range(N + 1):
            if current[i] != '.' and i + 1 < N + 2 and current[i + 1] != '.': 
                for k in range(N + 2):
                    if k + 1 < len(current) and current[k] == '.' and current[k + 1] == '.':
                        new_state = deepcopy(current)
                        new_state[k], new_state[k + 1] = current[i], current[i + 1]
                        new_state[i], new_state[i + 1] = '.', '.'
                        
                        # # デバッグ: 新しい状態を表示
                        # print(f"New state: {new_state}")

                        if tuple(new_state) not in visited:
                            visited.add(tuple(new_state))
                            queue.append((new_state, moves + 1))

    return -1

N = int(input())
S = input()
T = input()

result = bfs(N, S, T)
print(result)