class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # we can use a hashset to track the instance of 1) a value that does not occur
        # between the range [1, n^2] and 2) a value that occurs twice. 

        # for each value encountered in the matrix, add it to the hash set. For 
        # 2), if a value that exists in the hashset is discovered in the matix, let
        # a = value. For 1) iterate through the hashset using an incrementer. If the value at 
        # i+1 does not exist, let b = value. Return [a, b]
        numSet = set()
        a, b = None, None

        for row in grid:
            for value in row:
                if value in numSet:
                    a = value
                else:
                    numSet.add(value)
        #print(len(numSet))
        for i in range(1, len(numSet) + 2):
            #print(i)
            if i not in numSet:
                b = i
                break

        return [a, b]