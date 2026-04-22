class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        indices = {}

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                sum = nums[i] + nums[j]
                diff = 0 - sum

                if diff in indices:
                    if (j, i) in indices[diff]:
                        continue

                    indices[diff].append((i, j))
                else:
                    indices[diff] = [(i,j)]

        #print(list(indices.items()))
        res = []

        for i in range(len(nums)):
            if nums[i] not in indices:
                continue

            indexes = indices[nums[i]]
            for pair in indexes:
                if i in pair:
                    continue

                triplet = [nums[i], nums[pair[0]], nums[pair[1]]]
                triplet.sort()

                if triplet not in res:
                    res.append(triplet)

        return res