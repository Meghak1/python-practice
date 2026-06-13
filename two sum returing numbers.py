def two_sum(nums, target:int):
    sum_to_index={}
    for index, num in enumerate(nums):
        complement = target-num
        if complement in sum_to_index:
            return [complement, num]
        sum_to_index[num] = index
    return []
nums = [1,4,3,5,9]
k = 9
res = two_sum(nums, k)
print(res)
