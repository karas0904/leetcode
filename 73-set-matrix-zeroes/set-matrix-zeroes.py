class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def markRow(matrix, i):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0 and matrix[i][j] != -675:
                    matrix[i][j] = -675
        
        def markCol(matrix, j):
            for i in range(len(matrix)):
                if matrix[i][j] != 0 and matrix[i][j] != -675:
                    matrix[i][j] = -675

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    markRow(matrix, i)
                    markCol(matrix, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -675:
                    matrix[i][j] = 0