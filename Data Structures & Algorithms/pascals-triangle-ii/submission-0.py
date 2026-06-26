class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalsTriangle = [[] for i in range(rowIndex+1)]
        print(pascalsTriangle)

        for i, row in enumerate(pascalsTriangle):
            for _ in range(i+1):
                row.append(0)
            row[0] = 1
            row[-1] = 1

        #print(pascalsTriangle)
        for i, row in enumerate(pascalsTriangle):
            for j, num in enumerate(row):
                if num != 0:
                    continue
                row[j] = pascalsTriangle[i-1][j-1] + pascalsTriangle[i-1][j]

        #print(pascalsTriangle)
        return pascalsTriangle[rowIndex]

        