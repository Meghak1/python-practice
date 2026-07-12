class Solution:

    # Function to return intersection of two sorted arrays
    def findIntersection(self, arr1, arr2, n, m):

        i, j = 0, 0
        intersection = []
        last = None

        while i < n and j < m:

            if arr1[i] < arr2[j]:
                i += 1

            elif arr1[i] > arr2[j]:
                j += 1

            else:
                if last != arr1[i]:
                    intersection.append(arr1[i])
                    last = arr1[i]

                i += 1
                j += 1

        return intersection


# Driver Code
obj = Solution()

arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 2, 4, 6]

print(obj.findIntersection(arr1, arr2, len(arr1), len(arr2)))
