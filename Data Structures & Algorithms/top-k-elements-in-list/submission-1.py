class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        tally = defaultdict(int)
        #print(f"Buckets: {buckets}\nTally: {tally}")
        while len(nums) != 0:
            element = nums.pop()
            tally[element] += 1
        
        finalTally = dict(tally)

        for item in finalTally:
            freq = finalTally[item]
            buckets[freq].append(item)

        print(f"Buckets: {buckets}\nTally: {finalTally}")
        topKFreqElements = []

        counter = len(buckets) - 1
        #print(3)
        while len(topKFreqElements) < k:
            #print(2)
            if buckets[counter] != []:
                while len(topKFreqElements) < k and len(buckets[counter]) > 0:
                    #print(1)
                    topKFreqElements.append(buckets[counter].pop())
            counter -= 1

        #print(f"Return: {topKFreqElements}")
        return topKFreqElements




