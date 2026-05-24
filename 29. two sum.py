class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in sum_to_index:
                return [sum_to_index[complement], index]
            sum_to_index[num] = index
        return []
