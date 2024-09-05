class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def row_zero(row: int):
            for c in range(len(matrix[0])):
                matrix[row][c] = 0
        
        def col_zero(col: int):
            for r in range(len(matrix)):
                matrix[r][col] = 0

        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # First pass: Find all rows and columns that need to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # Second pass: Zero out all rows that need to be zeroed
        for r in zero_rows:
            row_zero(r)

        # Third pass: Zero out all columns that need to be zeroed
        for c in zero_cols:
            col_zero(c)