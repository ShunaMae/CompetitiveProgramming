def combine_adjacent_pairs(nums):
    results = []
    n = len(nums)
    
    for i in range(n - 1):
        new_list = nums[:i] + [int(str(nums[i]) + str(nums[i + 1]))] + nums[i + 2:]
        results.append(new_list)
    
    return results

def main():
    n = int(input())
    s = [int(z) for z in list(input())]

    if n == 2:
        print(int(str(s[0]) + str(s[1])))
        return 
    
    if 0 in s:
        print(0)
        return 
    
    combined = combine_adjacent_pairs(s)
    min_val = 10**19
    for lst in combined:
        min_val = min(min_val, sum(lst))
    
    print(min_val)

t = int(input())
for _ in range(t):
    main()
    
    
