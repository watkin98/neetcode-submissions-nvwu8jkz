class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # create a map to extract and track the instances of ints in nums
        mapping = {}
        smallestNum = nums[0]
        greatestNum = nums[0]

        # traverse nums and insert each instance of a num in map
        for num in nums:
            mapping[num] = True
            # save the smallest num for tracking
            if num < smallestNum:
                smallestNum = num
            # save the greatest num for tracking
            if num > greatestNum:
                greatestNum = num

        #print(f"Mapping: {mapping.items()}\nSmallest Num: {smallestNum}\nGreatest Num: {greatestNum}")

        # create a var to store the longest consecutive sequence and 
        # a sequence that's being evaluated
        lcs = 1
        lcsSoFar = 1
        i = smallestNum
        # starting from the smallest num, traverse the map by increments
        # of 1 and increment the lcs var
        while i <= greatestNum:
            increment = smallestNum + 1
            print(f"Increment: {increment}")
            if increment in mapping:
                lcsSoFar += 1
            else:
                if lcsSoFar > lcs:
                    lcs = lcsSoFar
                    lcsSoFar = 0
                    print("!!!")
                    print(f"Broke! LCS, LCS so far: {lcs}, {lcsSoFar}")
                else:
                    lcsSoFar = 0
            # if sequence is broken, store the lcs and reset eval sequence

            
            print(f"LCS So Far: {lcsSoFar}")
            i += 1
            smallestNum += 1
        print(f"LCS: {lcs}")
        return lcs

