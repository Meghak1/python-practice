class Solution:
    def findUnion(self, a, b):
        # code here 
        n = len(a)
        m = len(b)
        set1 = set(a)
        set2 = set(b)
        unionres = set1.union(set2)
        return sorted(unionres)
