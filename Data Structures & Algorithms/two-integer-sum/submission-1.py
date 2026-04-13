class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            print(diff)
            print(storage.items())
            if diff in storage:
                print(1)
                print("Should be returning!")
                print(f"Pair: [{i}, {storage[diff]}]")
                return [storage[diff], i]

            storage[nums[i]] = i

        return [-1, -1]