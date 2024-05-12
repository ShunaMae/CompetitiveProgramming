N = int(input())
A = list(map(int, input().split()))

from bisect import bisect_left

A.sort()

# 全ペアの和を求めるために、各要素が全ペアに寄与する総和を計算する
total_sum = sum(A) * (N - 1)

# 和が10**8以上のペアのカウント
cnt = 0
for i in range(N):
    # 和が10**8を超える最小のjを探す
    limit = 10**8 - A[i]
    idx = bisect_left(A, limit, i + 1)  # 自分自身を除外するため i + 1 から探す
    cnt += N - idx  # idx以降の要素数が条件を満たす

# 和が10**8を超えるペアの総和がどれだけ余分か計算する
excess = cnt * 10**8

result = total_sum - excess
print(result)
