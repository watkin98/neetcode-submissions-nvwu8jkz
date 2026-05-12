class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        res = []

        for num in nums:
            frequency[num] += 1

        tmp = list(frequency.items())

        freq_list = [[] for num in nums]
        freq_list.append([])

        for pair in tmp:
            freq_list[pair[1]].append(pair[0])

        for i in range(len(freq_list)-1, 0, -1):
            for j in range(0, len(freq_list[i])):
                res.append(freq_list[i][j])

                if len(res) == k:
                    return res