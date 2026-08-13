class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        count = start = 0

        while count < n:
            current_index = start
            prev = nums[current_index]

            while True:
                next_index = (current_index + k) % n
                nums[next_index], prev = prev, nums[next_index]
                count += 1
                current_index = next_index

                if current_index == start:
                    break

            start += 1