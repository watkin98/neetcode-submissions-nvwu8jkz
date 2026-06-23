class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a, b = -1, -1
        numSet = set()

        for col in grid:
            for val in col:
                if val in numSet:
                    a = val
                else:
                    numSet.add(val)

        for i in range(1, len(numSet) + 2):
            if i not in numSet:
                return [a, i]