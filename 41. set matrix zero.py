class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_column = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero_row.add(i)
                    zero_column.add(j)
        for i in range(m):
            for j in range(n):
                if i in zero_row or j in zero_column:
                    matrix[i][j]=0
        
