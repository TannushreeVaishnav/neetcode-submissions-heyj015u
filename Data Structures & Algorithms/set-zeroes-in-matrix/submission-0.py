class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,col=set(),set()
        n,m=len(matrix),len(matrix[0])

        for i in range (n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for  i in row:
            matrix[i]=[0]*m
        for j in col:
            for i in range(n):
                matrix[i][j]=0
        
        