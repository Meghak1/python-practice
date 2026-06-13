class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        currmap = {0:1}
        
        for num in nums:
            curr_sum+=num
            if curr_sum-k in currmap:
                count+=currmap[curr_sum-k]
            if curr_sum in currmap:
                currmap[curr_sum]+=1
            else:
                currmap[curr_sum] =1
        return count
