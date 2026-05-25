class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        res = []
        for num in nums:
            if num>0:
                positive.append(num)
            else:
                negative.append(num)
        res = []
        for n in range(len(positive)):
            res.append(positive[n])
            res.append(negative[n])
        return res
