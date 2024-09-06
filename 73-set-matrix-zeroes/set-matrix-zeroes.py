class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        INF = float('inf')
        def markRow(matrix, i):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0 and matrix[i][j] != INF:
                    matrix[i][j] = INF
        
        def markCol(matrix, j):
            for i in range(len(matrix)):
                if matrix[i][j] != 0 and matrix[i][j] != INF:
                    matrix[i][j] = INF

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    markRow(matrix, i)
                    markCol(matrix, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == INF:
                    matrix[i][j] = 0