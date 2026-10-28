class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) * len(matrix)

        l, r = 0, n - 1
        while l <= r:
            m = (l+r) // 2
            row = m // len(matrix[0])
            col = m % len(matrix[0])
            num = matrix[row][col]

            if num > target:
                r = m - 1
            elif num < target:
                l = m + 1
            else:
                return True
        return False