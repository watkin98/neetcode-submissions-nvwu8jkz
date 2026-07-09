class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numSet = set()
            for num in row:
                if num == '.':
                    continue
                if num in numSet:
                    return False
                numSet.add(num)

        for i in range(9):
            numSet = set()
            for j in range(9):
                num = board[j][i]
                if num == '.':
                    continue
                if num in numSet:
                    return False
                numSet.add(num)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                validBoard = self.isValidBoard(board, i, j, i+2, j+2)
                if validBoard is False:
                    return False
            
        return True

    def isValidBoard(self, board: List[List[str]], row1, col1, row2, col2) -> bool:
        numSet = set()
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                num = board[i][j]
                if num == '.':
                    continue
                if num in numSet:
                    return False
                numSet.add(num)
        return True
        
            