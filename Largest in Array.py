class Solution:
    def largest(self, arr):
        largest = 0
        for num in arr:
            if num > largest:
                largest = num
        return largest
        
