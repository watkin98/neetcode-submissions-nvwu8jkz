class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        buckets = [[] for i in range(len(nums)+1)]
        #print(f"buckets1: {buckets}")
        #buckets = [[]] * (len(nums)+1)
        #print(f"buckets2: {buckets}")
        #help(frequencies.get)

        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)

        print(f"frequencies: {frequencies.items()}")
        
        for num, freq in frequencies.items():
            buckets[freq].append(num)

        print(f"buckets: {buckets}")
        result = []

        for i in range(len(buckets)-1, 0, -1):
            for j in range(len(buckets[i])):
                result.append(buckets[i][j])
                if len(result) == k:
                    return result
