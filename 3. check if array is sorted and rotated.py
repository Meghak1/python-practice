class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        count = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i%n]>nums[(i+1)%n]:
                count+=1
        return count<=1
