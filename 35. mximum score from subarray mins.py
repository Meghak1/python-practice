class Solution:
    def maxSum(self, arr):
        # code here
        curr_sum = 0
        max_sum = 0
        for i in range(len(arr)-1):
            curr_sum = arr[i]+arr[i+1]
            max_sum = max(curr_sum, max_sum)
        return max_sum
