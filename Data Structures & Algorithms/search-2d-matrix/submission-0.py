class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l, r = matrix[i][0], matrix[i][-1]

            if target > l and target < r:
                row = matrix[i]
                l, r = 0, len(row) - 1

                while l <= r:
                    m = l + ((r-l) // 2)

                    if row[m] < target:
                        l = m + 1
                    elif row[m] > target:
                        r = m - 1
                    else:
                        return True

                return False

        return False

