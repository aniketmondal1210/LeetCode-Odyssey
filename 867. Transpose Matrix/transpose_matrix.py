class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        r = len(matrix)
        c = len(matrix[0])
        result = []
        for j in range(c):
            row = []
            for i in range(r):
                row.append(matrix[i][j])
            result.append(row)
        return result
