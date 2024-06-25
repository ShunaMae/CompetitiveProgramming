def combine_adjacent_pairs(nums):
    results = []
    n = len(nums)
    
    for i in range(n - 1):
        # 新しいリストを作成して、隣接するペアを結合
        new_list = nums[:i] + [int(str(nums[i]) + str(nums[i + 1]))] + nums[i + 2:]
        results.append(new_list)
    
    return results



def main():
    n = int(input())
    s = [int(z) for z in list(input())]

    ls = combine_adjacent_pairs(s)

    if n == 2:
        print(int(str(s[0]) + str(s[1])))
        return 
    
    is_zero = False
    is_one = False
    
    for l in ls:
        if 0 in l:
            is_zero = True
        if 1 in l:
            is_one = True


    if is_zero:
        print(0)
        return 
    
    
    
    combined = combine_adjacent_pairs(s)
    min_val = 10**19
    for lst in combined:
        while 1 in lst:
            lst.remove(1)
        
        if lst:
            cnt = sum(lst)
        else:
            cnt = 1
        min_val = min(min_val, cnt)
    

    print(min_val)

t = int(input())
for _ in range(t):
    main()
    
# main()