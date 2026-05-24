class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        curr_map = {}
        curr_sum = 0
        max_sum = 0
        for i in range(len(arr)):
            curr_sum +=arr[i]
            if curr_sum ==k:
                max_sum = i+1
            if curr_sum-k in curr_map:
                max_sum = max(max_sum, i-curr_map[curr_sum-k])
            if curr_sum-k not in curr_map:
                curr_map[curr_sum]=i
            elif not curr_sum:
                return 0
        return max_sum
