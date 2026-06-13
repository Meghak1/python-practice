class Solution:
    def leaders(self, arr):
        # code here
        leaders = []
        max_right = arr[-1]
        leaders.append(max_right)
        for i in range(len(arr)-2, -1, -1):
            if arr[i]>=max_right:
                leaders.append(arr[i])
                max_right = arr[i]
        leaders.reverse()
        return leaders
        
