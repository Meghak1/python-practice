class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len= 0
        curr_len = 0
        for num in nums:
            if num == 1:
                curr_len +=1
                max_len = max(curr_len,max_len)   
            else:
                curr_len = 0            
        return max_len
