from collections import defaultdict

# 入力の取得
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の計算
csum = [0] * (2 * N + 1)
for i in range(1, 2 * N + 1):
    csum[i] = (csum[i - 1] + A[(i - 1) % N]) % M

d = defaultdict(int)
ans = 0

csum = csum[:-1]

# 初期状態で、最初のN個の累積和を辞書に格納
for i in range(1, N + 1):
    d[csum[i]] += 1
# 左端点を全探索しながらカウント
for i in range(1, N + 1):
    # 右端を追加する
    ans += d[csum[i + N - 1]]
    # 左端の累積和を削除
    d[csum[i]] -= 1
    # 新しい右端の累積和を追加
    d[csum[i + N]] += 1

print(ans)