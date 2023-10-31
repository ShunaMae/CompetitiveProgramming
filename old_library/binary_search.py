# 二分探索
# 値を判定してbooleanを返すjudge関数を実装する

def judge(x):
    if x: return True 
    else: return False 

def binary_search(s, l, x):
    left = s-1
    right = l+1 
    while abs(left - right) > 1:
        mid = (right - left) // 2 
        if judge(x):
            left = mid 
        else:
            right = mid 

    return left 
    

print(binary_search(1, 100, 10))
