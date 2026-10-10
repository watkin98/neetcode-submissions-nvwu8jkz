"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(grid_n, grid_pos):
            if not grid_n:
                return None

            value = grid[int(grid_pos[0])][int(grid_pos[1])]
            new_node = Node(value, True, None, None, None, None)

            for i in range(int(grid_pos[0]), grid_n + int(grid_pos[0])):
                for j in range(int(grid_pos[1]), grid_n + int(grid_pos[1])):
                    if grid[i][j] != value:
                        new_node.isLeaf = False
                        break
                if not new_node.isLeaf:
                    break
            
            if new_node.isLeaf:
                return new_node

            new_node.topLeft = dfs(int(grid_n / 2), grid_pos)
            new_node.topRight = dfs(int(grid_n / 2), (grid_pos[0], grid_pos[1] + int(grid_n / 2)))
            new_node.bottomLeft = dfs(int(grid_n / 2), (grid_pos[0] + int(grid_n / 2), grid_pos[1]))
            new_node.bottomRight = dfs(int(grid_n / 2), (grid_pos[0] + int(grid_n / 2), grid_pos[1] + int(grid_n / 2)))

            return new_node

        return dfs(n, (0, 0))