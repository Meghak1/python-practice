from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = max(freq, key = freq.get)
        return res
