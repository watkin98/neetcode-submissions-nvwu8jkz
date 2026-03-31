class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numTally = defaultdict(int)
        mostFreqElems = []

        for num in nums:
            numTally[num] += 1

        numList = []
        for num, count in numTally.items():
            numList.append([count, num])
        print(f"numList before sort: {numList}")
        numList.sort()
        print(f"numList after sort: {numList}")

        #print(f"Number Tally: {numTally}")

        mostFreq = []

        while len(mostFreq) < k:
            mostFreqElem = numList.pop()
            mostFreq.append(mostFreqElem[1])

        return mostFreq





