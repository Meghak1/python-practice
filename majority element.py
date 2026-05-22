class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        vote = 0

        for num in nums:
            if vote ==0:
                candidate = num
            if candidate ==num:
                vote+=1
            else:
                vote -=1

        return candidate
