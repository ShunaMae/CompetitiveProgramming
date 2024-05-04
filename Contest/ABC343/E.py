class Node:
    def __init__(self):
        self.max_val = 0  # 最大値
        self.max_count = 0  # 最大値の出現回数
        self.second_max_val = 0  # 2番目に大きい値
        self.second_max_count = 0
    
def merge(left, right):
    node = Node()
    # 最大値の更新
    if left.max_val > right.max_val:
        node.max_val = left.max_val
        node.max_count = left.max_count
        if left.second_max_val > right.max_val:
            node.second_max_val = left.second_max_val
            node.second_max_count = left.second_max_count
        elif left.second_max_val < right.max_val:
            node.second_max_val = right.max_val
            node.second_max_count = right.max_count
        else:  # left.second_max_val == right.max_val
            node.second_max_val = right.max_val
            node.second_max_count = right.max_count + left.second_max_count
    elif left.max_val < right.max_val:
        node.max_val = right.max_val
        node.max_count = right.max_count
        if right.second_max_val > left.max_val:
            node.second_max_val = right.second_max_val
            node.second_max_count = right.second_max_count
        elif right.second_max_val < left.max_val:
            node.second_max_val = left.max_val
            node.second_max_count = left.max_count
        else:  # right.second_max_val == left.max_val
            node.second_max_val = left.max_val
            node.second_max_count = left.max_count + right.second_max_count
    else:  # left.max_val == right.max_val
        node.max_val = left.max_val
        node.max_count = left.max_count + right.max_count
        node.second_max_val = max(left.second_max_val, right.second_max_val)
        if left.second_max_val > right.second_max_val:
            node.second_max_count = left.second_max_count
        elif left.second_max_val < right.second_max_val:
            node.second_max_count = right.second_max_count
        else:  # left.second_max_val == right.second_max_val
            node.second_max_count = left.second_max_count + right.second_max_count
    return node



def update(tree, index, val, node=1, start=0, end=None):
    if end is None:
        end = len(tree) // 2 - 1
    if start == end:
        # 葉のノードを更新
        tree[node].max_val = val
        tree[node].max_count = 1
        # ここでは2番目に大きい値は存在しないので、デフォルト値を設定
        tree[node].second_max_val = -1  # 適切なデフォルト値に設定
        tree[node].second_max_count = 0
        return
    mid = (start + end) // 2
    if index <= mid:
        update(tree, index, val, node * 2, start, mid)
    else:
        update(tree, index, val, node * 2 + 1, mid + 1, end)
    tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

def query(tree, L, R, node=1, start=0, end=None):
    if end is None:
        end = len(tree) // 2 - 1
    if R < start or end < L:
        # 範囲外のクエリに対しては、無効な値を持つ Node を返す
        dummy = Node()
        dummy.max_val = -float('inf')
        dummy.second_max_val = -float('inf')
        return dummy
    if L <= start and end <= R:
        return tree[node]
    mid = (start + end) // 2
    left_result = query(tree, L, R, node * 2, start, mid)
    right_result = query(tree, L, R, node * 2 + 1, mid + 1, end)
    return merge(left_result, right_result)

def build_segment_tree(N):
    size = 1
    while size < N:
        size *= 2
    size *= 2  # 木全体のサイズ
    tree = [Node() for _ in range(size)]
    return tree



def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    # セグメントツリーの構築
    tree = build_segment_tree(N)
    for i, val in enumerate(A):
        update(tree, i, val)

    # クエリの処理
    for _ in range(Q):
        query_type, l, r = map(int, input().split())
        if query_type == 1:
            # タイプ1のクエリ：位置 l の値を r に更新
            update(tree, l - 1, r)  # 0-indexedに調整
        else:
            # タイプ2のクエリ：区間 [l, r] の2番目に大きい値の個数を出力
            result = query(tree, l - 1, r - 1)  # 0-indexedに調整
            print(result.second_max_count)

if __name__ == "__main__":
    main()
