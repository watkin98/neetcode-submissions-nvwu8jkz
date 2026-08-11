class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        res = []
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

        new_nums = list(numbers.items())
        # print(f"Numbers: {new_nums}")
        # new_nums.sort()
        # print(f"Numbers: {new_nums}")

        while len(res) < k:
            most_freq = new_nums[0]
            # print(f"most_freq: {most_freq}")
            for i in range(len(new_nums)):
                if new_nums[i][1] > most_freq[1] and new_nums[i][0] not in res:
                    most_freq = new_nums[i]

            res.append(most_freq[0])
            # print(f"most_freq: {most_freq}")
            # print(f"res: {res}")

        return res