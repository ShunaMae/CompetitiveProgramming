A, B, C = map(int, input().split())

if B < C:
    # 寝ている時間帯が日付をまたがない場合
    if B <= A < C:
        print("No")
    else:
        print("Yes")
else:
    # 寝ている時間帯が日付をまたぐ場合
    if A >= B or A < C:
        print("No")
    else:
        print("Yes")