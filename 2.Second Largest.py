class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        lar = sec = -1
        for num in arr:
            if num >lar:
                sec = lar
                lar = num
            elif num >sec and num!=lar:
                sec = num
        return sec

#gfg
