class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numTally = {}
        numBuckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numTally[num] = 1 + numTally.get(num, 0)

        print(f"numTally: {numTally}\nnumTally.items(): {list(numTally.items())}")

        for num, tally in numTally.items():
            numBuckets[tally].append(num)

        print(f"numBuckets: {numBuckets}")

        result = []

        #while len(result) < k:
        for i in range(len(numBuckets) - 1, 0, -1):
            if len(result) == k:
                return result
            for j in range(len(numBuckets[i])):
                print(2)
                if len(result) < k:
                    print(3)
                    result.append(numBuckets[i][j])
                else:
                    print(f"result: {result}")
                    return result

        return result